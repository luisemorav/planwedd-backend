from cloudinary import config, uploader
from os import getenv

class Cloudinary:
    def __init__(self):
        config(
            cloud_name=getenv('CLOUD_NAME'),
            api_key=getenv('API_KEY'),
            api_secret=getenv('API_SECRET')
        )

    def uploadImage(self, file):
        try:
            result = uploader.upload(file)
            return result['secure_url']
        except Exception as err:
            raise err
        