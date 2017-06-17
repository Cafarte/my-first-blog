from django.conf.urls import include, url
from base5 import views
urlpatterns = [
    url(r'^$', views.post_list),
]