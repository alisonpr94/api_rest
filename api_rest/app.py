from fastapi import FastAPI
from api_rest.schemas import UserSchema, UserPublic
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/', status_code=200)
def read_root():
    return RedirectResponse("/docs/")

@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    return user
