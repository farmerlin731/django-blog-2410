from django.contrib.auth import views as django_auth_views
from django.urls import path, reverse_lazy

from users import views as user_views

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
    path("register/", user_views.register, name="register"),
    path(
        "password/change/",
        django_auth_views.PasswordChangeView.as_view(
            template_name="users/pwd_change.html",
            success_url=reverse_lazy("users:password_change_done"),
            # success_url=reverse_lazy("blog:post-list"),
        ),
        name="password_change",
    ),
    path(
        "password/change/done/",
        django_auth_views.PasswordChangeDoneView.as_view(
            template_name="users/pwd_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password/reset/",  # 填寫 email 要求重設密碼信件
        django_auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html",
            email_template_name="users/email/password_reset_content.html",
            subject_template_name="users/email/password_reset_subject.txt",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password/reset/done/",  # 信件寄出後的頁面
        django_auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password/reset/<uidb64>/<token>/",  # 信件中的 url，讓使用者可以重設密碼
        django_auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password/reset/complete/",  # 重設密碼成功後顯示的頁面
        django_auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
