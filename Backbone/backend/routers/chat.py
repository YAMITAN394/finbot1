from fastapi import APIRouter, HTTPException
from backend.utils.logger import setup_logger
from backend.config import settings

router = APIRouter()
logger = setup_logger()

@router.get("/chat/{query}")
async def ai_chat(query: str):
    try:
        # If Google services are configured, use Google AI Platform
        if settings.google_project_id and settings.google_credentials:
            from google.cloud import aiplatform
            model = aiplatform.Model("gemini-pro")
            result = model.predict(instances=[{"prompt": query}])
            ai_response = result.predictions[0]

            # Log to Firestore if available
            try:
                from backend.utils.firestore_db import get_firestore_db
                db = get_firestore_db()
                db.collection("chat_history").add({
                    "user_query": query,
                    "ai_response": ai_response
                })
            except Exception as e:
                logger.error(f"Firestore logging error: {e}")
        
        # Fallback to a simple response if Google services are not configured
        else:
            ai_response = "I apologize, but the AI chat service is currently not configured. Please try again later."
            logger.warning("Google AI services not configured, returning fallback response")
        
        return {"response": ai_response}
        
    except Exception as e:
        logger.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail="Error processing chat request")
