from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        case = ['Установить python', 'Установить django', 'Запустить сервер', 'Порадоваться результату', 'Пятый пункт!']
        tags_case = []
        for i in case:
            tags_case.append(f'<li>{i}</li>')
        response_case = f'<ul>{"".join(tags_case)}</ul>'
        return HttpResponse(response_case)
