from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from image_manager.controller.images import ImageAPI, ImagesAPI, TagsAPI

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

api.add_resource(ImagesAPI, '/images/')
api.add_resource(ImageAPI, '/image/<int:image_id>/')
api.add_resource(TagsAPI, '/tags/')

if __name__ == "__main__":
    app.run(debug=True)
