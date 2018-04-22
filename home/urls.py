from django.conf.urls import url
from .views import HomePage


# We are adding a URL called /home
urlpatterns = [
    url(r'^$', HomePage.as_view(), name="home"),
]