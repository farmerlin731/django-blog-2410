from django.contrib.auth import views as django_auth_views
from django.urls import path

app_name = "users"

# Class-based views
# Must add "as.view()" before.
urlpatterns = [path("login/", django_auth_views.LoginView.as_view(), name="login")]
