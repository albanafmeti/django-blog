from django.shortcuts import render


def index(request):
    data = {"hello": "world"}
    return render(request, "blog/index.html", context=data)
