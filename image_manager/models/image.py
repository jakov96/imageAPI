from app import db, ma
from config import ALLOWED_EXTENSIONS

association_table = db.Table('association',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('image_id', db.Integer, db.ForeignKey('image.id'), primary_key=True)
)


class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __str__(self):
        return self.name

class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String, unique=True)
    tags = db.relationship('Tag', secondary=association_table, backref=db.backref('images', lazy=True))

    @classmethod
    def allowed_file(cls, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    @classmethod
    def create(cls, image):
        image = cls(
            name=image['name'],
            url=image['url'],
        )

        db.session.add(image)
        db.session.commit()

        return image


class ImageSchema(ma.Schema):
    class Meta:
        model = Image
        sqla_session = db.session
        fields = ('id', 'name', 'url')


class TagSchema(ma.Schema):
    class Meta:
        model = Tag
        sqla_session = db.session
        fields = ('id', 'name')