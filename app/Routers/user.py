from .. import schemas,models,utils,oath2
from fastapi import FastAPI, HTTPException, Response, status, Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
router=APIRouter(prefix='/users', tags=['Users'])
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate,db: Session=Depends(get_db)):
    hashpassword=utils.hashpass(user.password)
    user.password=hashpassword
    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get("/",response_model=List[schemas.UserResponse])
def users(db: Session=Depends(get_db),):
    #cursor.execute('''Select * from posts''')
    #posts=cursor.fetchall() 
    #return {"data":posts}
    users=db.query(models.User).all()
    return users   
@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id:int, db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with {id} not found')
    return user
