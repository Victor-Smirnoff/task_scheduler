from fastapi import FastAPI
import uvicorn
from fastapi.responses import ORJSONResponse


app = FastAPI(
    title="Планировщик задач",
    docs_url="/api/docs",
    openapi_url="/api/docs/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.get("/")
async def root():
    return {"message": "Test STRING!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
