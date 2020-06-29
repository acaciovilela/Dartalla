from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard")
]
