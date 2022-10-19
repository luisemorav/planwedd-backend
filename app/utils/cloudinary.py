from cloudinary import config, uploader

class Cloudinary:
    def __init__(self):
        self.cloud_name = "de3i8hs61"
        self.api_key = "697852552381113"
        self.api_secret = "SGthDnSL6NpdHh6TloTBl-crRPk"
        config(
            cloud_name=self.cloud_name,
            api_key=self.api_key,
            api_secret=self.api_secret
        )

    def uploadImage(self, file):
        try:
            result = uploader.upload(file)
            return result['secure_url']
        except Exception as err:
            raise err
        