from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


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

# TODO с этими классами проблема, возможно в шаблонах ошибки
class Contacts(TemplateView):
    template_name = 'advertisement/contacts.html'

    def contacts(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ['8-800-708-19-45', '8-800-708-19-45', '8-800-708-19-45']
        context['title'] = 'Контакты'
        context['emails'] = ['sales@company.com', 'sales@company.com', 'sales@company.com']
        context['address'] = ['city-1', 'city-2', 'city-3', 'city-4', 'city-5']
        return context


class Companies(TemplateView):
    template_name = 'advertisement/companies.html'

    def company(self, **kwargs):
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