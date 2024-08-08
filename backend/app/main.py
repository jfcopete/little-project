from fastapi import FastAPI
from .routers import user_router, album_router, track_router
from .database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(album_router.router)
app.include_router(track_router.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)