from django.urls import include, path

urlpatterns = [
    path("api/v1/rephrase/", include("apps.rephrase.api.routes")),
]
