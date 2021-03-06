from django.shortcuts import render
from . import models
from django.views import View, generic


class Index(View):
    def get(self, request):
        return render(request, 'advertisements_app/index.html')


class AdvertisementsListView(generic.ListView):
    model = models.Advertisement


class AdvertisementsDetailView(generic.DetailView):
    model = models.Advertisement

    def count(self, request):
        modell = models.Advertisement.objetts.get(id=self.model.pk)
        modell.views_count += 1
        modell.save()
        return render(request, 'advertisements_app/advertisement_detail.html',
                      {'counts': modell.views_count})
