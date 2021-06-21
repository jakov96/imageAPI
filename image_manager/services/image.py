import os
from flask_restful import abort
from werkzeug.utils import secure_filename
import uuid


class ImageService:
    @staticmethod
    def read_all(tags=None):
        from image_manager.models.image import Image, ImageSchema, Tag

        if tags:
            images = Image.query.filter(Image.tags.any(Tag.id.in_(tags))).all()
        else:
            images = Image.query.all()

        image_schema = ImageSchema(many=True)
        return {
            'results': image_schema.dump(images),
            'count': len(images)
               }, 200

    @staticmethod
    def read_one(image_id):
        from image_manager.models.image import Image, ImageSchema
        image = Image.query.filter(Image.id == image_id).one_or_none()

        if image:
            image_schema = ImageSchema()
            return image_schema.dump(image), 200

        abort(404)

    @staticmethod
    def create(image_data, tags_ids):
        from image_manager.models.image import Image, ImageSchema
        from app import app

        if Image.allowed_file(image_data.filename):
            image_name = '{}_{}'.format(str(uuid.uuid4()), secure_filename(image_data.filename))

            image_url = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

            image = Image.create({
                'name': secure_filename(image_data.filename),
                'url': image_url,
                'tags': tags_ids
            })

            if image:
                image_data.save(image_url)

                schema = ImageSchema()
                return schema.dump(image), 201

        abort(400, message='Недопустимый файл')
