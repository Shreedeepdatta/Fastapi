
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models

from .database import engine
from .Routers import post,user,authentication,vote
from .config import Settings
origins=["https://www.google.com"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def message():
    return{'message':'hello world'}
app.include_router(post.router)
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(vote.router)
#models.Base.metadata.create_all(bind=engine)



