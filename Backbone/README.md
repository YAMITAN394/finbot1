# Backend Service Setup

## Prerequisites

1. Google Cloud Project setup with the following services enabled:
   - Google Cloud Firestore
   - Google Cloud AI Platform
   - Google BigQuery

2. Environment Variables Required:
   ```
   GOOGLE_PROJECT_ID=your-project-id
   GOOGLE_CREDENTIALS=path-to-your-credentials.json
   ```

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up Google Cloud credentials:
   - Download your Google Cloud service account key
   - Set the GOOGLE_CREDENTIALS environment variable to point to your key file
   - Set the GOOGLE_PROJECT_ID environment variable

3. Database Setup:
   - Create a BigQuery dataset named 'market_data'
   - Create a table named 'stock_prices' with columns:
     - symbol (STRING)
     - price (FLOAT)
     - timestamp (TIMESTAMP)

## Running the Application

1. Start the server:
   ```bash
   python -m backend.main
   ```

2. The API will be available at:
   - Chat endpoint: `/chat/{query}`
   - Stock endpoint: `/stock/{symbol}`

## Notes

- The application now uses Google Cloud services instead of local connections
- All data is stored and retrieved from Google Cloud services
- Make sure your Google Cloud project has the necessary permissions and quotas