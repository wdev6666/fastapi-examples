from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    return {"data": f"Blog is created with title as {blog.title}"}

@app.get("/")
def index():
    return {"data": {"name": "Naresh"}}

@app.get("/blog")
def unpublished(limit: int = 10, published: bool = False):
    if published:
        return {"data": f"{limit} of published blogs"}
    else:
        return {"data": f"{limit} of unpublished blogs"}

@app.get("/blog/{id}")
def blog(id: int):
    return {"data": id}