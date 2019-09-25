from django.shortcuts import render
import datetime
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    # rendering the template in HttpResponse
    return HttpResponse(html)


@require_http_methods(["GET"])
def show(request):
    return HttpResponse('<h1>This is Http GET request.</h1>')
