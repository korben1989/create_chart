from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadfilesView.as_view(), name='index'),
    path('chart', views.ChartView.as_view(), name='chart'),

]