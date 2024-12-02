from fastapi import FastAPI, Depends, HTTPException
from .dependencies import get_current_user
from fastapi import status
import uvicorn

app = FastAPI(title="Service A", root_path="/service-a")

@app.get("/")
def hello_service_a(current_user = Depends(get_current_user)):
    if current_user.role == 'auser':
        return {"message": f"Hello A {current_user.username}!"}
    elif current_user.role == 'admin':
        return {"message": f"Hello admin {current_user.username}!"}
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Not authorized to access this service"
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)