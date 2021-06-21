from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from image_manager.controllers.images import ImageAPI, ImagesAPI, TagsAPI

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

api.add_resource(ImagesAPI, '/api/v1/images/')
api.add_resource(ImageAPI, '/api/v1/image/<int:image_id>/')
api.add_resource(TagsAPI, '/api/v1/tags/')

if __name__ == "__main__":
    app.run(debug=True)
