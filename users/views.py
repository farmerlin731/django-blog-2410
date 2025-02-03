import datetime

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

# Create your views here.


def set_cookies(request):
    data = request.GET.get("data", "farmerinit")
    now = timezone.now()  # UTC+0
    expire = now + datetime.timedelta(minutes=1)

    response = HttpResponse("okok")
    response.set_cookie("data", data, expires=expire)

    return response


def show_cookies(request):
    return HttpResponse(request.COOKIES.get("data"))


def delete_cookies(request):
    response = HttpResponse("Deleted.")
    response.delete_cookie("data")
    return response


def set_session(request):
    data = request.GET.get("data", "empty")
    request.session["data"] = data
    return HttpResponse("okok")


def show_session(request):
    return HttpResponse(request.session.get("data"))


def delete_session(request):
    if "data" in request.session:
        del request.session["data"]
    return HttpResponse("Session deleted.")


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("users:login")
    return render(request, "users/register.html", {"form": form})
