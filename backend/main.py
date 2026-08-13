
from fastapi import FastAPI

app = FastAPI(
    title="Construction Radar API",
    version="1.0.0",
    description="API для мониторинга строительных проектов"
)


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Construction Radar API",
        "version": "1.0.0"
    }


@app.get("/api/health")
def health():
    return {
        "status": "healthy"
    }
