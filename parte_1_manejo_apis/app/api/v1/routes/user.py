# app/api/v1/routes/user.py
from fastapi import APIRouter, HTTPException
from app.core.utils.constants import GET_USER_USER_NO_FOUND_404
from app.services.external_api import fetch_users

router = APIRouter()

@router.get("/users/")
async def get_user():
    user = await fetch_users()
    if not user:
        raise HTTPException(status_code=404, detail=GET_USER_USER_NO_FOUND_404)
    return user
