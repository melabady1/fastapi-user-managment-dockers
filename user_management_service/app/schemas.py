from pydantic import BaseModel, constr

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50)
    password: constr(min_length=6)
    role: str  # 'auser', 'buser', or 'admin'

class UserResponse(BaseModel):
    username: str
    role: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str