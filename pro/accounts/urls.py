#     url(r'^(?P<id>\d+)/delete/', delete_view, name='delete'),
# ]


from django.conf.urls import url,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = "accounts"

urlpatterns = [

    url(r'^login/$', login_view , name="login"),
    url(r'^post/$' , include('app.urls')),
    url(r'^register/$', register_view , name="register")
    # url(r'^create/$', create_view, name='create'),
    #
    # url(r'^(?P<slug>[\w-]+)/$', detail_view, name='detail'),
    #
    # url(r'^(?P<slug>[\w-]+)/update/$', update_view , name="update"),
    #
    # url(r'^(?P<slug>[\w-]+)/delete/$', delete_view , name="delete"),

    # url(r'^page404/$', notfound404_view , name="404"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)