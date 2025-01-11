from fastapi import FastAPI
from app.routes import bg_remove, enhance

app = FastAPI()

# Include the routers
app.include_router(bg_remove.router, tags=["Background Removal"])
app.include_router(enhance.router, tags=["Enhancement"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Image Processing API"}
