from django.http import HttpResponse


def display(request):
    response = '<h1>Welcome to Django</h1>'
    return HttpResponse(response)


def hello_world(request):
    response = '<h1>Hello World</h1>'
    return HttpResponse(response)


def good_morning(request):
    response = '<h1>Hello Good Morning</h1>'
    return HttpResponse(response)


def good_afternoon(request):
    response = '<h1>Hello Good Afternoon</h1>'
    return HttpResponse(response)


def good_evening(request):
    response = '<h1>Good Evening</h1>'
    return HttpResponse(response)
