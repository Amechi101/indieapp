from django.conf.urls import patterns, url

from product_extend.views import ProductView


urlpatterns = patterns('',
    url(r'^$', ProductView.as_view(),
        name='product_list'
        ),
    )
