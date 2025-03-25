# Change Log

## Changes to Implement

1. **Modify `backend/main.py`**:
   - Change the `uvicorn.run` line to prevent binding to localhost.
   - Ensure the application is configured to run in a cloud environment.

2. **Update `backend/config.py`**:
   - Verify that the environment variables `GOOGLE_PROJECT_ID` and `GOOGLE_CREDENTIALS` are set correctly in the deployment environment.

3. **Revise `backend/routers/chat.py`**:
   - Ensure the AI model is correctly configured to connect to Google services.

4. **Revise `backend/routers/stock.py`**:
   - Update the stock price retrieval logic to use a Google API for stock data.

5. **Check `backend/utils/firestore_db.py`**:
   - Ensure the Firestore client is initialized correctly with the necessary credentials.

## Additional Notes
- Ensure that all necessary Google Cloud services are enabled and configured in the Google Cloud Console.
- Test the application thoroughly after making these changes to ensure everything works as expected.