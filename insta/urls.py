from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    url('^$', views.index, name='index')
]