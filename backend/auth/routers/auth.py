import json
from fastapi import APIRouter, status
from model_config import UserRequest
from db_dependency import DB_DEPENDENCY
from models import Users
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

@router.get('/user')
async def get_user_auth(db: DB_DEPENDENCY):
    return db.query(Users).all()

@router.post("/user/submit", status_code=status.HTTP_201_CREATED)
async def user_submit(db:DB_DEPENDENCY, user_request: UserRequest):
    # user_address = json.dumps([address.model_dump() for address in user_request.addresses])
    create_user_model = Users(
        email = user_request.email,
        username = user_request.username,
        first_name = user_request.first_name,
        last_name = user_request.last_name,
        role = user_request.role,
        hased_password = bcrypt_context.hash(user_request.hased_password),
        is_active = user_request.is_active,
        # address = user_address
    )
    db.add(create_user_model)
    db.commit()
    return user_request


