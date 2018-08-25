# from django.conf.urls import url, include
# from .views import *
# app_name='app'
# urlpatterns = [
#     url(r'^index/$', index_view , name="index"),
#     url(r'^(?P<id>\d+)/', detail_view , name='detail'),
#     url(r'^create/$', create_view , name="create" ),
#     url(r'^(?P<id>\d+)/update/', update_view, name="update"),
#     url(r'^(?P<id>\d+)/delete/', delete_view, name='delete'),
# ]


from django.conf.urls import url
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = "app"

urlpatterns = [

    url(r'^index/$', index_view , name="index"),

    url(r'^create/$', create_view, name='create'),

    url(r'^(?P<slug>[\w-]+)/$', detail_view, name='detail'),

    url(r'^(?P<slug>[\w-]+)/update/$', update_view , name="update"),

    url(r'^(?P<slug>[\w-]+)/delete/$', delete_view , name="delete"),

    # url(r'^page404/$', notfound404_view , name="404"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)