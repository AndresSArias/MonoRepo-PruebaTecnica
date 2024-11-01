from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.utils.constants import CAPTURE_POKEMON_DESCRIPTION, CAPTURE_POKEMON_POKEMON_NO_FOUND_404, CAPTURE_POKEMON_SUMMARY, CAPTURE_POKEMON_USER_NO_FOUND_404, GET_CAPTURES_CAPTURES_NO_FOUND_404, GET_CAPTURES_DESCRIPTION, GET_CAPTURES_SUMMARY
from app.db.session import get_session
from app.models.capture import Capture
from app.services.external_api import fetch_user, fetch_pokemon

router = APIRouter()

#Endpoint con el cual haremos una captura, antes validado la existencia de las dos partes, la persona mediante su usuario y el pokemon mediante su id de pokédex o nombre.
@router.put("/capture/{username}/pokemon/{pokemon_name}", summary=CAPTURE_POKEMON_SUMMARY, description=CAPTURE_POKEMON_DESCRIPTION)
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

#Endpoint para mostrar las capturas realizadas.
@router.get("/captures",summary=GET_CAPTURES_SUMMARY,description=GET_CAPTURES_DESCRIPTION)
async def get_captures(session: Session = Depends(get_session)):
    captures = session.query(Capture).all()
    # Verificamos si la lista de capturas está vacía
    if not captures:
        raise HTTPException(status_code=404, detail=GET_CAPTURES_CAPTURES_NO_FOUND_404)
    
    return captures