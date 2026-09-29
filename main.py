from fastapi import FastAPI

app = FastAPI(
    title="Blockchain EHR API",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Blockchain EHR API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "ehr-api"
    }