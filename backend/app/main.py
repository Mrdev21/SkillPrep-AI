from fastapi import FastAPI

from app.api.auth import router as auth_router


app = FastAPI(
    title="SkillPrep AI",
    description="AI-powered interview training and career preparation platform",
    version="0.1.0",
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "SkillPrep AI backend is running",
        "status": "ok",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }