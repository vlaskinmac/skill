import time

from django.core.exceptions import PermissionDenied


class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ['127.0.0.1']
        # allowed_ips = ['']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response


class TimeSleepIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        if request.META.get('REMOTE_ADDR'):
            self.count += 1
        if self.count % 2 == 0:
            response = self.get_response(request)
            return response
        else:
            time.sleep(3)
            response = self.get_response(request)
            return response


class BlockTimeIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        self.started_at = time.time()  # TODO стартуем таймер
        request.META.get('REMOTE_ADDR') # TODO фиксируем ip запроса
        self.count += 1 # TODO считаем запросы
        self.ended_at = time.time() # TODO фиксируем время
        self.elapsed = self.ended_at - self.started_at
        if self.count > 1 and self.elapsed < 3: # TODO не более одного клика раз в три секунды
            raise PermissionDenied
        else:
            response = self.get_response(request)
            return response












