from flask_restful import abort


class TagService:
    @staticmethod
    def read_all():
        from image_manager.models.image import Tag, TagSchema
        tags = Tag.query.all()
        schema = TagSchema(many=True)
        return schema.dump(tags), 200

    @staticmethod
    def create(data):
        from image_manager.models.image import Tag, TagSchema
        from app import db

        tag_name = data.get('name')
        tag = Tag.query.filter(Tag.name == tag_name).one_or_none()

        if not tag:
            schema = TagSchema()
            new_tag = Tag(name=tag_name)
            print(new_tag)
            db.session.add(new_tag)
            db.session.commit()

            return schema.dump(new_tag), 201

        abort(400, message='Такой тег уже существует')
