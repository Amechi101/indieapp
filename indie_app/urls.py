from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from _backend_api.views import WebsiteView
# from product_extend.views import ProductView


from django.contrib import admin

urlpatterns = patterns("",
    url(r"^$", WebsiteView.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/social/", include("social.apps.django_app.urls", namespace="social")),
    url(r"^account/", include("account.urls")),
    url(r'^browse/', include('_backend_api.urls')), 
    url(r'^scrap_api/', include('scrap.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
