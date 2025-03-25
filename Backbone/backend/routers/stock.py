from fastapi import APIRouter, HTTPException
from backend.utils.logger import setup_logger
from backend.config import settings
import yfinance as yf

router = APIRouter()
logger = setup_logger()

@router.get("/stock/{symbol}")
async def get_stock_price(symbol: str):
    try:
        # If Google services are configured, use BigQuery
        if settings.google_project_id and settings.google_credentials:
            from google.cloud import bigquery
            client = bigquery.Client(project=settings.google_project_id)
            query = f"""
                SELECT price 
                FROM `{settings.google_project_id}.market_data.stock_prices`
                WHERE symbol = @symbol
                ORDER BY timestamp DESC
                LIMIT 1
            """
            job_config = bigquery.QueryJobConfig(
                query_parameters=[
                    bigquery.ScalarQueryParameter("symbol", "STRING", symbol)
                ]
            )
            query_job = client.query(query, job_config=job_config)
            results = query_job.result()
            
            for row in results:
                return {"symbol": symbol, "price": row.price}
                
            raise HTTPException(status_code=404, detail="Stock price not found")
        
        # Fallback to yfinance if Google services are not configured
        else:
            ticker = yf.Ticker(symbol)
            price = ticker.info.get('regularMarketPrice')
            if price is None:
                raise HTTPException(status_code=404, detail="Stock price not found")
            return {"symbol": symbol, "price": price}
            
    except Exception as e:
        logger.error(f"Error fetching stock price for {symbol}: {e}")
        raise HTTPException(status_code=400, detail="Error fetching stock price")
