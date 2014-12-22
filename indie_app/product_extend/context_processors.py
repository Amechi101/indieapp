import cloudinary
def constsHomepage(request):
    return dict(
        THUMBNAIL = {
            "class": "thumbnail inline", "format": "jpg", "crop": "limit", "height": 150, "width": 150,
        },
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
