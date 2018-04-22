from django.conf.urls import url
from . import views

urlpatterns = [
    # Register related URLs
    url(r'^$',views.register_new, name='register_new'),
]