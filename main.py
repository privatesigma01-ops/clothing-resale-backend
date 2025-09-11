from fastapi import FastAPI
from routers import clothing

app = FastAPI()

app.include_router(clothing.router, prefix="/api/clothing")

@app.get("/")
def root():
    return {"message": "Welcome to the Clothing Resale Platform"}
