from django.conf.urls import url
from . import views
from .views import StudentList

# We are adding a URL called /home
urlpatterns = [
    url(r'^$',views.home, name='index'),
    url(r'^list/$',StudentList.as_view(), name='student_list'),
    url(r'^new/$',views.student_cru, name='student_new'),
    url(r'^(?P<uuid>[\w-]+)/$',views.student_detail, name='student_detail'),
    url(r'^(?P<uuid>[\w-]+)/edit/$',views.student_cru, name='student_update'),
]