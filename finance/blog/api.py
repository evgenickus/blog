from ninja import NinjaAPI
# from ninja.security import django_auth
from typing import List, Optional
from blog.models import User, Article, Comment
from blog.schema import UserRegistrationSchema, UserSchema, ArticleSchema, CommentSchema



api = NinjaAPI(csrf=True)

@api.get("/users", response=List[UserSchema])
def users(request):
  return User.objects.all()
  


@api.get("/article")#, auth=django_auth)
def article(request):
  # # return request.auth
  data = [a for a in Article.objects.all()]
  res = [ArticleSchema(name = d.name, author=d.author.username) for d in data]
  return res

@api.get("/comment", response=List[CommentSchema])
def comment(request):
  return Comment.objects.all()



@api.post('/regisration')
def regisration(request, payload: UserRegistrationSchema):
  if len(User.objects.filter(username__iexact=payload.username)) == 0 and len(User.objects.filter(email__iexact=payload.email)) == 0:
    newuser = User.objects.create(**payload.dict())
    return f'user : {newuser.username} has been created'
  elif len(User.objects.filter(username__iexact=payload.username)) > 0:
    return {'message': f'user with username : {payload.username} exists'}
  elif len(User.objects.filter(email__iexact=payload.email)) > 0:
    return {'message': f'user with email : {payload.email} exists'}

  
      
@api.post('/addpost')
def addpost(request, payload: ArticleSchema):
    user = User.objects.get(id=payload.author)
    newpost = Article.objects.create(name=payload.name, author=user)
    return {'message': f'added new article : {newpost.name}'}

@api.post('/addcomment/')
def addcomment(request, payload: CommentSchema):
    user = User.objects.get(id=payload.author)
    article = Article.objects.get(pk=payload.article)
    newcomment = Comment.objects.create(text=payload.comment, article=article, author=user)
    return {'message': f'added new comment : {newcomment.text}'}



    
       