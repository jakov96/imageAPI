from flask import request
from flask_restful import Resource, abort
from image_manager.services.image import ImageService
from image_manager.services.tag import TagService


class ImageAPI(Resource):
    def get(self, image_id):
        return ImageService.read_one(image_id)


class ImagesAPI(Resource):
    def get(self):
        tags = request.args.getlist('tags')

        return ImageService.read_all(tags)

    def post(self):
        if 'image' in request.files:
            tags = request.form.to_dict().get('tags')

            try:
                tags_ids = [int(x) for x in tags.split(',')]
                return ImageService.create(request.files['image'], tags_ids), 201
            except ValueError:
                abort(400, message='Недопустимое значение параметра tags')

        return abort(400, message="Не передан обязательной параметр image")


class TagsAPI(Resource):
    def get(self):
        return TagService.read_all()

    def post(self):
        if request.json and 'name' in request.json:
            return TagService.create(request.json)

        abort(400, message='Неверный запрос')

