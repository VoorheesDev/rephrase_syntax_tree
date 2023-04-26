from apps.rephrase.api.views import CreateRephrasedTreesAPIView
from django.urls import path

urlpatterns = [
    path("", CreateRephrasedTreesAPIView.as_view(), name="create_rephrased_trees"),
]
