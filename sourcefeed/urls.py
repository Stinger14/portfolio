from django.urls import path

from .views import PythonFeedView

urlpatterns = [
    path("", PythonFeedView.as_view(), name="python_content"),
]
