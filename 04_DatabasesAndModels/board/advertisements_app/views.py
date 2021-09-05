from django.shortcuts import render
from . import models
from django.views import View


def index(request, *args, **kwargs):
    return render(request, 'advertisements_app/index.html')


def advertisements(request, *args, **kwargs):
    advertisements_list = models.Advertisement.objects.all()
    return render(request, 'advertisements_app/list_adver.html', {
        'advertisements_list': advertisements_list
    })


class Advertisements(View):
    count = 0

    def get(self, request):
        Advertisements.count += 1
        advertisements_list = models.Advertisement.objects.all()
        return render(request, 'advertisements_app/details_adver.html', {'advertisements_list': advertisements_list,
                                                                         'counts': Advertisements.count})


