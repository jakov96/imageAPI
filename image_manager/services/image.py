import os
from flask_restful import abort
from werkzeug.utils import secure_filename
import uuid


class ImageService:
    @staticmethod
    def read_all():
        from image_manager.models.image import Image, ImageSchema
        images = Image.query.all()
        image_schema = ImageSchema(many=True)
        return image_schema.dump(images), 200

    @staticmethod
    def read_one(image_id):
        from image_manager.models.image import Image, ImageSchema
        image = Image.query.filter(Image.id == image_id).one_or_none()

        if image:
            image_schema = ImageSchema()
            return image_schema.dump(image), 200

        abort(404)

    @staticmethod
    def create(data):
        from image_manager.models.image import Image, ImageSchema
        from app import app

        if Image.allowed_file(data.filename):
            image_name = '{}_{}'.format(str(uuid.uuid4()), secure_filename(data.filename))

            image_url = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

            image = Image.create_image({
                'name': image_name,
                'url': image_url
            })

            if image:
                data.save(image_url)

                schema = ImageSchema()
                return schema.dump(image), 201

        abort(400, message='Недопустимый файл')
