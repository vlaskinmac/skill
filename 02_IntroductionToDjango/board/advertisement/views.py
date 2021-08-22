from django.shortcuts import render


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html')


def course_1(request, *args, **kwargs):
    return render(request, 'advertisement/course_1.html')


def course_2(request, *args, **kwargs):
    return render(request, 'advertisement/course_2.html')


def course_3(request, *args, **kwargs):
    return render(request, 'advertisement/course_3.html')


def course_4(request, *args, **kwargs):
    return render(request, 'advertisement/course_4.html')
