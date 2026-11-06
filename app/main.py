"""Aplicação FastAPI independente do PhotoBooth."""

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from app.routes.photobooth import router as photobooth_router

app = FastAPI(
    title="NexUs PhotoBooth API",
    description="API de envio das fotos da Expotech pelo GREEN-API.",
    version="1.0.0",
)
app.include_router(photobooth_router)


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
