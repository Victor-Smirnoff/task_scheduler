from fastapi import FastAPI
import uvicorn
from fastapi.responses import ORJSONResponse


app = FastAPI(
    title="Планировщик задач",
    docs_url="/api/docs",
    openapi_url="/api/docs/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup_event():
    print("Приложение запущено...")


@app.on_event("shutdown")
async def shutdown_event():
    print("Приложение выключено...")


@app.get("/")
async def root():
    return {"message": "Test STRING!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
