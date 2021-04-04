from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    url('', views.home, name='home'),
    #url( r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    
]