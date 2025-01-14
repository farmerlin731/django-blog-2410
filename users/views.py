import datetime

from django.http import HttpResponse
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
