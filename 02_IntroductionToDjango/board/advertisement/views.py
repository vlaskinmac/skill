from django.shortcuts import render


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html')


def course_1(request, *args, **kwargs):
    return render(request, 'advertisement/course_1.html')
