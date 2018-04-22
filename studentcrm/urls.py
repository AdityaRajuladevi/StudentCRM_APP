"""studentcrm URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include HomePage URL
    url(r'^', include('home.urls')),

    # Include Registrations URL
    url(r'^signup/', include('register.urls')),

    # Login/Logout URLs
    url(r'^login/$', views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/'}),

    # Include Students App urls
    url(r'^students/', include('students.urls')),
    # Include Contact App Urls
    url(r'^contacts/', include('contacts.urls')),
]
