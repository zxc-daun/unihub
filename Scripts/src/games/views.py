from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseForbidden, HttpResponseBadRequest, HttpResponseServerError

def index(request):
    return HttpResponse("<h1>Home Page - Страница приложения</h1>.")

def categories(request, categories_id):
    if request.GET:
        print(request.GET)

    return HttpResponse(f"<h1>categories id is: </h1><p>{categories_id}</p>")

def archive(request, year):
    if int(year) > 2023:
        return redirect('homepage', permanent = False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена 404</h1>")

def pageForbidden(request, exception):
    return HttpResponseForbidden("<h1> Permission Denied Sorry(</h1>")

def HttpResponseBadRequest(request, exception):
    return HttpResponseBadRequest("<h1> Bad Request Sorry(<h1>")

# def HttpResponseServerError(request, exception):
#     return HttpResponseServerError("<h1> Server Error Sorry(<h1>")

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)