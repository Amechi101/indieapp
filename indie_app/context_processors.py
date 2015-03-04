import cloudinary

def consts(request):
    return dict(
        BRANDIMAGE = {
        	"format": "jpg", "crop": "fill"
        },
        THUMBNAIL = {
        	"format": "png", "crop": "fill","height":120,"width":120
        },
        PRODUCT = {
           "format": "jpg", "crop": "fill",  "width": 300
        },
        CLOUDINARY_CLOUD_NAME = cloudinary.config().cloud_name
    )
