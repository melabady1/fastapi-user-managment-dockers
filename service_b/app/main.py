from fastapi import FastAPI, Depends, HTTPException
from .dependencies import get_current_user
from fastapi import status
import uvicorn

app = FastAPI(title="Service B", root_path="/service-b" )

@app.get("/")
def welcome_service_b(current_user = Depends(get_current_user)):
    if current_user.role == 'buser':
        return {"message": f"Welcome B {current_user.username}!"}
    elif current_user.role == 'admin':
        return {"message": f"Welcome admin {current_user.username}!"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Not authorized to access this service"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)