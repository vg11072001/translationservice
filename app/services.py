from google.cloud import translate_v2 as translate
from app.models import TranslationLog
from fastapi import HTTPException
import os

# Initialize Google Translate client
try:
    client = translate.Client()
except Exception as e:
    raise RuntimeError(
        "Google Translate client initialization failed. Make sure credentials are set."
    ) from e


def translate_text(text: str, target_language: str) -> str:
    try:
        result = client.translate(text, target_language=target_language)
        return result.get("translatedText", "")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Translation failed: {str(e)}"
        )


def log_translation(
    original_text: str,
    target_language: str,
    translated_text: str,
    endpoint: str,
    request_type: str,
):
    log = TranslationLog(
        original_text=original_text,
        target_language=target_language,
        endpoint=endpoint,
        translated_text=translated_text,
        request_type=request_type,
    )
    log.save()
