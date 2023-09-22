from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadfilesView.as_view(), name='index'),

]