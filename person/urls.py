from django.urls import path

from person.views import ListPersonView

app_name = "person"

urlpatterns = [
    path("person/", ListPersonView.as_view(), name="list")
]
