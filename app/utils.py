from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
def hashpass (password:str):
    return pwd_context.hash(password)
def verifypass (plainpass,hashpass):
    return pwd_context.verify(plainpass, hashpass)