from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import initialize_database
from routes.users import user_router
from routes.meters import meter_router
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialize_database()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(user_router, prefix="/user")
app.include_router(meter_router, prefix="/meter")

@app.get("/")
async def home():
    return RedirectResponse(url="/meter/")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
