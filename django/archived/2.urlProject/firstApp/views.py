from django.http import HttpResponse


def first_view(request):
    return HttpResponse('First View')


def second_view(request):
    return HttpResponse('Second View')


def third_view(request):
    return HttpResponse('Third View')


def fourth_view(request):
    return HttpResponse('Fourth View')


def fifth_view(request):
    return HttpResponse('Fifth View')
