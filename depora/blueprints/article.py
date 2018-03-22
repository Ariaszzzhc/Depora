from flask import Blueprint
from flask_restful import Resource, reqparse, Api
from depora.utils import mongo

article_blueprint = Blueprint(
    'article',
    __name__,
    url_prefix='/api/article'
)

article_api = Api(article_blueprint)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('content', type=str)
parser.add_argument('author', type=str)
parser.add_argument('date', type=str)


class Article(Resource):
    def get(self, article_id):
        cursor = mongo.db.articles.find_one({'article_id': article_id})
        article = {
            'article_id': cursor['article_id'],
            'title': cursor['title'],
            'content': cursor['content'],
            'author': cursor['author'],
            'date': cursor['date']
        }
        return article, 200

    def post(self, article_id):
        args = parser.parse_args(strict=True)
        article = {
            'article_id': article_id,
            'title': args['title'],
            'content': args['content'],
            'author': args['author'],
            'date': args['date']
        }
        mongo.db.articles.insert(article)
        return 201


article_api.add_resource(Article, '/<int:article_id>')

