from django.http import HttpResponse

# Create your views here.


def set_cookies(request):
    data = request.GET.get("data", "farmerinit")

    response = HttpResponse("okok")
    response.set_cookie("data", data)

    return response


def show_cookies(request):
    return HttpResponse(request.COOKIES.get("data"))


def delete_cookies(request):
    response = HttpResponse("Deleted.")
    response.delete_cookie("data")
    return response
