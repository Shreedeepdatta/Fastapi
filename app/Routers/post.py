from .. import schemas,models,oath2
from fastapi import FastAPI, HTTPException, Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
from sqlalchemy import func
router=APIRouter(prefix="/posts", tags=['Posts'])
@router.get("/",response_model=List[schemas.PostOut])
def posts(db: Session=Depends(get_db),user_id:int=Depends(oath2.get_current_user),limit:int=2,skip:int=0,search:Optional[str]=""):
    #cursor.execute('''Select * from posts''')
    #posts=cursor.fetchall() 
    #return {"data":posts}
    #posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    posts=db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote,models.Vote.post_id==models.Post.id,
    isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def createposts(posts:schemas.PostCreate,db: Session=Depends(get_db),user_id:int=Depends(oath2.get_current_user)):
    print(user_id)
    newpost=models.Post(owner_id=user_id.id,**posts.dict())
    db.add(newpost)
    db.commit()
    db.refresh(newpost)
    
    return newpost

@router.get("/{id}",response_model=schemas.PostOut)
def get_posts(id:int, db: Session=Depends(get_db),user_id:int=Depends(oath2.get_current_user)):
    #post_query=db.query(models.Post).filter(models.Post.id==id)
    #post=post_query.first()
    post=db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote,models.Vote.post_id==models.Post.id,
    isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        """ response.status_code= status.HTTP_404_NOT_FOUND
        return {"message": f"post with id {id} was not found"} """
    #if post.Post.owner_id!=user_id.id:
    #    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'You dareth do that you filthy peasant')
    return post

@router.delete("/{id}")
def delete_post(id:int, db:Session=Depends(get_db),user_id:int=Depends(oath2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id {id} does not exist')
    if post.owner_id!=user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Not authorized')
    post_query.delete(synchronize_session=False)
    db.commit() 
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/posts/{id}',response_model=schemas.PostResponse)
def update_post(id:int, updated_post: schemas.PostBase, response:Response, db: Session=Depends(get_db),user_id:int=Depends(oath2.get_current_user)):
   post_query=db.query(models.Post).filter(models.Post.id==id)
   post=post_query.first()
   if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post does not exist with id:{id}')
   if post.owner_id!=user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Not authorized')
   post_query.update(updated_post.dict(),synchronize_session=False)
   db.commit()
   return {"post detail": post_query.first()}
