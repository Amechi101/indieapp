import cloudinary

def consts(request):
    return dict(
        THUMBNAIL = {
            "class": "thumbnail inline", "format": "jpg", "crop": "fit", "height": 90, "width": 90,
        },
        PRODUCT = {
           "format": "jpg", "crop": "fit", "height": 400, "width": 400,
        },
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
