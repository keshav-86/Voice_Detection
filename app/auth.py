from fastapi import Header, HTTPException

SECRET_API_KEY = "sk_test_123456"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != SECRET_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
