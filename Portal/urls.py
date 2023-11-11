from django.contrib import admin
from django.urls import path
# from spms import views as spms_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('spms/', spms_views.urls),
    path('', views.index, name='index'),
]
