from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List
from app.services import translate_text, log_translation
from app.models import TranslationLog

router = APIRouter()

class TranslationRequest(BaseModel):
    text: str = Field(..., max_length=1000, description="Text to be translated")
    target_language: str = Field(..., min_length=2, max_length=5, description="Target ISO language code (e.g., 'hi', 'en')")

class TranslationResponse(BaseModel):
    translated_text: str

@router.post("/translate", response_model=TranslationResponse)
def translate_post(request: TranslationRequest):
    translated_text = translate_text(request.text, request.target_language)
    log_translation(request.text, request.target_language, translated_text, request_type="POST", endpoint="/api/translate")
    return {"translated_text": translated_text}

@router.get("/translate", response_model=TranslationResponse)
def translate_get(
    text: str = Query(..., description="Text to be translated"),
    target_language: str = Query(..., min_length=2, max_length=5, description="Target ISO language code (e.g., 'hi', 'en')")
):
    if len(text) > 1000:
        # Split the text into chunks of 1000 characters or less
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        translated_chunks = [translate_text(chunk, target_language) for chunk in chunks]
        translated_text = "\n\n\n".join(translated_chunks)
        log_translation(text, target_language, translated_text, request_type="GET", endpoint="/api/translate")
        return {"translated_text": translated_text}
    else:
        translated_text = translate_text(text, target_language)
        log_translation(text, target_language, translated_text, request_type="GET", endpoint="/api/translate")
        return {"translated_text": translated_text}