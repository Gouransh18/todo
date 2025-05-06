from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import get_db, engine  # Add engine to the import
import models

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to TodoList API"}

@app.get("/api/todos")
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return {"todos": todos}

@app.get("/api/profiles")
def get_profiles(db: Session = Depends(get_db)):
    profiles = db.query(models.Profile).all()
    return {"profiles": profiles}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)