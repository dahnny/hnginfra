from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class MessageResponse(BaseModel):
    message: str


class MeResponse(BaseModel):
    name: str
    email: str
    github: str


app = FastAPI(
    title="Minimal FastAPI Application",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
    default_response_class=JSONResponse,
)


@app.get("/", response_model=MessageResponse, status_code=status.HTTP_200_OK)
def read_root() -> MessageResponse:
    return MessageResponse(message="API is running")


@app.get("/health", response_model=MessageResponse, status_code=status.HTTP_200_OK)
def read_health() -> MessageResponse:
    return MessageResponse(message="healthy")


@app.get("/me", response_model=MeResponse, status_code=status.HTTP_200_OK)
def read_me() -> MeResponse:
    return MeResponse(
        name="Your Full Name",
        email="you@example.com",
        github="https://github.com/yourusername",
    )