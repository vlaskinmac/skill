from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class Contacts(TemplateView):
    template_name = 'advertisement/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ['8-800-708-19-45', '8-800-708-19-45', '8-800-708-19-45']
        context['title'] = 'Контакты'
        context['emails'] = ['sales@company.com', 'sales@company.com', 'sales@company.com']
        context['address'] = ['city-1', 'city-2', 'city-3', 'city-4', 'city-5']
        return context


class Companies(TemplateView):
    template_name = 'advertisement/companies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_company'] = 'any_name_company'
        context['title'] = 'О Компании'
        context['description'] = 'any_description'
        return context


class CBV(View):
    def get(self, request):
        list_advertisement = ['объявление 1', 'объявление 2', 'объявление 2', 'объявление 4', 'объявление 5', ]
        return render(request, 'advertisement/list_adver.html', {'list_adver': list_advertisement})

    def post(self, request):
        count = 0
        method_post = request.META.get('REQUEST_METHOD')
        if method_post:
            count += 1
        return render(request, 'advertisement/count_post.html', {'counts': count})


class AdvertisementList(View):
    def get(self, request):
        list_regions = ['region 1', 'region 2', 'region 3', 'region 4', 'region 5', ]
        return render(request, 'advertisement/advertisement_list.html', {'regions': list_regions })

