import os
from app import db
from image_manager.models.image import Image

if os.path.exists('image.db'):
    os.remove('image.db')

db.create_all()
db.session.commit()
