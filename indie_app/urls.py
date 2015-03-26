from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from indie_app.views import HomepageView

from django.contrib import admin

urlpatterns = patterns("",
    url(r"^$", HomepageView.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/social/", include("social.apps.django_app.urls", namespace="social")),
    url(r"^account/", include("subscription.urls")),
    url(r"^account/", include("account.urls")),
    url(r"^brand/", include('_backend_api.urls')), 
    url(r"^ajax_login/$", TemplateView.as_view(template_name="_global_partials/ajax_login_brand_follow.html")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
