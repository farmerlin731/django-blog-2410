from django.contrib.auth import views as django_auth_views
from django.urls import path

app_name = "users"

# Class-based views
# Must add "as.view()" before.
urlpatterns = [
    # path(
    #     "login/",
    #     django_auth_views.LoginView.as_view(template_name="users/login.html"),
    #     name="login",
    # )
    path(
        "login/",
        django_auth_views.LoginView.as_view(
            template_name="users/login.html",
            # True means u won't seee the login-page if u have already logined.
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout/", django_auth_views.LogoutView.as_view(), name="logout"),
]
