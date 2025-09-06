from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from .models import ShortenRequest, ShortenResponse
from .config import settings
from .utils import gen_code, normalize_url
from .db import get_url, put_url, code_exists

app = FastAPI(title="URL Shortener")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/shorten", response_model=ShortenResponse)
def shorten(req: ShortenRequest):
    long_url = normalize_url(str(req.url))
    code = gen_code(settings.CODE_LENGTH)
    tries = 0
    while code_exists(code):
        code = gen_code(settings.CODE_LENGTH)
        tries += 1
        if tries > 5:
            raise HTTPException(status_code=500, detail="Failed to allocate code")
    put_url(code, long_url)
    return ShortenResponse(code=code, short_url=f"{settings.BASE_URL}/{code}", long_url=long_url)

@app.get("/{code}")
def resolve(code: str):
    long_url = get_url(code)
    if not long_url:
        raise HTTPException(status_code=404, detail="Not found")
    return RedirectResponse(url=long_url, status_code=307)
