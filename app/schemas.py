from pydantic import BaseModel,EmailStr
from typing import Optional
from pydantic.types import conint
class PostBase(BaseModel):
    title: str  
    content: str
    published: bool=True

class UserResponse(BaseModel):
    email:EmailStr
    id:int
    class Config:
        orm_mode=True

class PostCreate(PostBase):
    pass
class PostResponse(BaseModel):
    title:str
    content:str
    publlished:bool=True
    id:int
    owner_id:int 
    owner:UserResponse
    class Config:
        orm_mode=True
class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str
class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:Optional[int] = None
class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)
class PostOut(BaseModel):
    Post: PostResponse
    votes:int
    class Config:
        orm_mode=True