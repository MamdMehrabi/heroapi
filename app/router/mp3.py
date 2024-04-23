from fastapi import APIRouter, Response, status
from fastapi.responses import FileResponse

import pyttsx3

router = APIRouter(prefix='/api', tags=['Text to voice'])


@router.get('/text2voice', status_code=status.HTTP_200_OK)
@router.post('/text2voice', status_code=status.HTTP_200_OK)
async def text_to_voice(responce: Response, text: str) -> dict:
    '''Convert text to voice (without artificial intelligence)'''
    FILE_PATH = 'app/tmpfiles/speech.mp3'
    engine = pyttsx3.init()
    engine.save_to_file(text=text, filename=FILE_PATH)
    engine.runAndWait()
    return FileResponse(FILE_PATH)