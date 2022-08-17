from blog import schemas, models, token
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog.hashing import Hash

def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user or not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials!")
    access_token = token.create_access_token(data = {"sub": user.email})
    return {"access_token": access_token, "token_Type": "bearer"}