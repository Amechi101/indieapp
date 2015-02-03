import cloudinary

def consts(request):
    return dict(
        BRANDIMAGE = {
        	"format": "jpg", "crop": "fill"
        },
        THUMBNAIL = {
        	"format": "png", "crop": "fill","height":90,"width":90
        },
        PRODUCT = {
           "format": "jpg", "crop": "fill", "height": 400, "width": 400
        },
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
