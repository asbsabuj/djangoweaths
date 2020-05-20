from django.shortcuts import render


def first(request):
    return render(request, 'hello.html', {})


def second(request):
    return render(request, 'locations.html', {})