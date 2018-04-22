from django.conf.urls import url

from contacts.views import ContactDelete
from . import views

urlpatterns = [
    url(r'^new/$',views.contact_cru, name='contact_new'),
    url(r'^(?P<uuid>[\w-]+)/edit/$',views.contact_cru, name='contact_update'),
    url(r'^(?P<pk>[\w-]+)/delete/$',ContactDelete.as_view(), name='contact_delete'),
]