from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='url_home'),
    path('details', views.details, name='url_dtl'),
    path('fonts', views.fonts),
    path('downloadd', views.download_view),
    path('aaa', views.aaa)
]
