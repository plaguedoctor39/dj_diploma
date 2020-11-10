from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^login$', views.MyLoginView.as_view(), name='login_page'),
    url(r'^register$', views.RegisterUserView.as_view(), name='register_page'),
    url(r'^logout$', views.MyLogout.as_view(), name='logout'),
]
