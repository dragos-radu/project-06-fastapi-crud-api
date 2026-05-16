from fastapi import FastAPI

app = FastAPI(
    title = "DevOps Projects API",
    description = "A simple FastAPI CRUD API for managing DevOps portfolio projects.",
    version = "1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}