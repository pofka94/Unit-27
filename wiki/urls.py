from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:page_id>/", views.detail, name="detail"),
    path("<int:page_id>/results/", views.results, name="results"),
]