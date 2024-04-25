from ninja import Router
from .models import Article
from users.models import User
from .schemas import ArticleSchema

router = Router()


@router.get("/")#, auth=django_auth)
def articles(request):
  # # return request.auth
  data = [a for a in Article.objects.all()]
  res = [ArticleSchema(name = d.name, author=d.author.username) for d in data]
  return res


@router.post('/')
def addarticle(request, payload: ArticleSchema):
    user = User.objects.get(id=payload.author)
    newpost = Article.objects.create(name=payload.name, author=user)
    return {'message': f'added new article : {newpost.name}'}