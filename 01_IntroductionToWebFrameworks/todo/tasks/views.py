from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        # TODO не уверен что правильно прописал! Или нужно списку присвоить переменную и переменную
        #  передать в класс HttpResponse?
        return HttpResponse(['<ul>''<li>Установить python</li>''<li>Установить django</li>' '<li>Запустить сервер</li>'
                             '<li>Порадоваться результату</li>' '<li>Пятый пункт!</li>''</ul>'])
