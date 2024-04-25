from ninja import Router
from users.models import User
from typing import List
from .schemas import UserRegistrationSchema, UserSchema

router = Router()

@router.get("/", response=List[UserSchema])
def users(request):
  return User.objects.all()


@router.post('/')
def adduser(request, payload: UserRegistrationSchema):
  if len(User.objects.filter(username__iexact=payload.username)) == 0 and len(User.objects.filter(email__iexact=payload.email)) == 0:
    newuser = User.objects.create(**payload.dict())
    return f'user : {newuser.username} has been created'
  elif len(User.objects.filter(username__iexact=payload.username)) > 0:
    return {'message': f'user with username : {payload.username} exists'}
  elif len(User.objects.filter(email__iexact=payload.email)) > 0:
    return {'message': f'user with email : {payload.email} exists'}