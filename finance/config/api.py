from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

api.add_router('/users/', 'users.api.router')
api.add_router('/articles/', 'articles.api.router')
api.add_router('/comments/', 'comments.api.router')