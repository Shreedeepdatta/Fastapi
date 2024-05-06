from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import database
from .. import models,schemas,utils,oath2
router=APIRouter(tags=['Authentication'])
@router.post('/login',response_model=schemas.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    if not utils.verifypass(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    access_token=oath2.createaccesstoken(data={"user_id": user.id})
    return {"access_token":access_token, "token_type": "bearer"}
   