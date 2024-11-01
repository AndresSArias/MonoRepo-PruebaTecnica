from typing import List
from fastapi import APIRouter, HTTPException
from app.core.utils.constants import GET_USERS_USERS_DESCRIPTION, GET_USERS_USERS_NO_FOUND_404, GET_USERS_USERS_SUMMARY
from app.schemas.user import UserResponse
from app.services.external_api import fetch_users

router = APIRouter()

#Endpoint que traer todas las personas disponibles para capturar un pokémon.
@router.get("/users/", response_model=List[UserResponse], summary=GET_USERS_USERS_SUMMARY,description=GET_USERS_USERS_DESCRIPTION)
async def get_users():
    user = await fetch_users()
    if not user:
        raise HTTPException(status_code=404, detail=GET_USERS_USERS_NO_FOUND_404)
    return user
