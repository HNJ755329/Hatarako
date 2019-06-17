
from django.urls import path
from . import views

urlpatterns = [
    path("", views.hataraku_index, name="hataraku_index"),
    path("result", views.hataraku_result, name="hataraku_result"),
    path("<uuid:uuid>/", views.hataraku_uuid, name="hataraku_uuid"),
]