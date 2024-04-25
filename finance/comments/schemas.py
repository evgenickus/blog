from ninja import Schema

class CommentSchemaIn(Schema):
  comment: str
  username: str
  article: str

class CommentSchemaOut(Schema):
  comment: str
  username: str
  article: str
  author: str
