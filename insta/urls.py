
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

from django.contrib.auth.views import LoginView

from django.conf import settings

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^signup/$',views.sign_up, name="signup"),
    url('^login/$', LoginView.as_view(template_name='registration/login.html')),
    url('^logout/$', views.logout_view, name='logout'),
    url('^user_profile/$', views.user_profile, name='profile'),
    url('^user_details/$', views.user_detail, name='home'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]