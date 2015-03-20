from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from indie_app.views import HomepageView

from django.contrib import admin

urlpatterns = patterns("",
    url(r"^$", HomepageView.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/social/", include("social.apps.django_app.urls", namespace="social")),
    url(r"^account/", include("account.urls")),
    url(r"^brand/", include('_backend_api.urls')), 
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
