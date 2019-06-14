from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.count),
    url(r'^clear$', views.clear),
]

