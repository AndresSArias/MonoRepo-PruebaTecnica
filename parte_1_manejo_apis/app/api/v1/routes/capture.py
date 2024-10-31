# app/api/v1/routes/capture.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.utils.constants import CAPTURE_POKEMON_POKEMON_NO_FOUND_404, CAPTURE_POKEMON_USER_NO_FOUND_404, GET_CAPTURES_CAPTURES_NO_FOUND_404
from app.db.session import get_session
from app.models.capture import Capture
from app.services.external_api import fetch_user, fetch_pokemon

router = APIRouter()

@router.put("/capture/{username}/pokemon/{pokemon_name}")
async def capture_pokemon(username: str, pokemon_name: str, session: Session = Depends(get_session)):
    user = await fetch_user(username)

    if not user:
        raise HTTPException(status_code=404, detail= CAPTURE_POKEMON_USER_NO_FOUND_404)

    pokemon = await fetch_pokemon(pokemon_name)
    if not pokemon:
        raise HTTPException(status_code=404, detail= CAPTURE_POKEMON_POKEMON_NO_FOUND_404)

    new_capture = Capture(username=username, pokemon_name=pokemon.name)
    session.add(new_capture)
    session.commit()
    return {"message": f"{user.name} capturó a un {pokemon.name}"}


@router.get("/captures")
async def get_captures(session: Session = Depends(get_session)):
    captures = session.query(Capture).all()
    # Verificamos si la lista de capturas está vacía
    if not captures:
        raise HTTPException(status_code=404, detail=GET_CAPTURES_CAPTURES_NO_FOUND_404)
    
    return captures