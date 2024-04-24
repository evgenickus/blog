import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
from psycopg2 import sql

dataBase = psycopg2.connect(
    # dbname='postgres',
    user="postgres",
    password="1",
    host="127.0.0.1",
    port="5432"
    )

dataBase.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 

cursorObject = dataBase.cursor()

cursorObject.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier("blog_db"))
    )
print("All Done")

"""
select ba."name" as "Название статьи", bu2.username as "Автор статьи", bc."text" as "Комментарий к статье", bu.username as "Автор комментария" from blog_comment bc
join blog_article ba on bc.article_id_id = ba.id 
join blog_user bu on bc.user_id_id = bu.id 
join blog_user bu2 on ba.author_id = bu2.id;
"""