
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

from django.contrib.auth.views import LoginView

from django.conf import settings

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^sign_up/$',views.sign_up, name="sign_up"),
    url('^login/$', LoginView.as_view(template_name='registration/login.html')),
    url('^log_out/$', views.logout_view, name='Log_out'),
    url('^user_profile/$', views.user_profile, name='profile'),
    url('^user_details/$', views.user_detail, name='home'),
    url(r'^password/$', views.change_password, name='change_password'),
]