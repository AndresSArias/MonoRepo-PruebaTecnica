# app/api/v1/routes/user.py
from fastapi import APIRouter, HTTPException
from app.services.external_api import fetch_users

router = APIRouter()

@router.get("/users/")
async def get_user():
    user = await fetch_users()
    if not user:
        raise HTTPException(status_code=404, detail="Users not found")
    return user
