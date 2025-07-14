from fastapi import APIRouter, HTTPException
from services.linkedin_service import LinkedInService

router = APIRouter()
service = LinkedInService()

@router.post("/login")
def login(username: str, password:str):
    try:
        service.perform_login(username, password)
        return {"message": "Login successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
