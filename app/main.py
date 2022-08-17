from typing import List
from hashlib import new
from statistics import mode
from fastapi import FastAPI, Depends, Response, status, HTTPException
from blog import models
from blog.database import  engine
from blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)