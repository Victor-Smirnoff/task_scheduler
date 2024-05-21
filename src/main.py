from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from logging import getLogger


app = FastAPI(
    title="API Планировщик задач",
    docs_url="/api/docs",
    openapi_url="/api/docs/openapi.json",
    default_response_class=ORJSONResponse,
)

logger = getLogger("elk")


@app.on_event("startup")
async def startup_event():
    logger.warning("WARNING:  Приложение API “Планировщик задач” запущено...")


@app.on_event("shutdown")
async def shutdown_event():
    logger.warning("WARNING:  Приложение API “Планировщик задач” выключено...")


@app.get("/")
async def root():
    return {"message": "Test STRING !"}
