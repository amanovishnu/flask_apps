from django.shortcuts import render
from datetime import datetime


def wish(request):
    return render(request, 'firstApp/wish.html')


def server_time(request):
    data = {'server_time': datetime.now()}
    return render(request, 'firstApp/wish.html', context=data)


def results(request):
    data = {
        "name": "amanovishnu",
        "roll_no": 1,
        "marks": 100,
        "date": datetime.now()
    }
    return render(request, 'firstApp/wish.html', context=data)


def wish_time(request):
    data = dict()
    date = int(datetime.now().strftime("%H"))
    print(date)
    if date < 12:
        data["msg"] = "Good Morning"
    elif date < 16:
        data["msg"] = "Good Afternoon"
    elif date < 20:
        data["msg"] = "Good Evening"
    else:
        data["msg"] = "Good Night"
    return render(request, 'firstApp/wish.html', context=data)
