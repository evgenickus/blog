from ninja import Schema

class UserRegistrationSchema(Schema):
  username: str
  first_name: str
  last_name: str
  email: str
  password: str

class UserSchema(Schema):
  username: str
  email: str