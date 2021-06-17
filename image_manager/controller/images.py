from flask import request
from flask_restful import Resource, abort
from image_manager.services.image import ImageService
from image_manager.services.tag import TagService


class ImageAPI(Resource):
    def get(self, image_id):
        return ImageService.read_one(image_id)


class ImagesAPI(Resource):
    def get(self):
        return ImageService.read_all()

    def post(self):
        if 'image' in request.files:
            return ImageService.create(request.files['image']), 201

        return abort(400, message="Не передан обязательной аргумент image")


class TagsAPI(Resource):
    def get(self):
        return TagService.read_all()

    def post(self):
        return TagService.create(request.json)
