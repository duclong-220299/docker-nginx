from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("download/<str:file_name>/", views.download, name="download"),
]
