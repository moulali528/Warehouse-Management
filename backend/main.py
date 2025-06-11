from database import engine
import models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routers import auth
from todos.routers import todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(auth.router) 
app.include_router(todos.router)