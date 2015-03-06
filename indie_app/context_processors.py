import cloudinary

def consts(request):
    return dict(
        BRANDIMAGE = {
        	"format": "jpg", "crop": "fill"
        },
        THUMBNAIL = {
        	"format": "jpg", "crop": "fill","height":300,"width":300
        },
        PRODUCT = {
           "format": "jpg", "crop": "fill",  "width": 400,  "height": 500
        },
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
