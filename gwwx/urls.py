from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from gwwx import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^wechat$', csrf_exempt(views.Wechat.as_view()), name="wechat"),
)
