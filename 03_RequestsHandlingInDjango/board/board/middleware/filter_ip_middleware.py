import time
from board.middleware import mod_logger
from django.core.exceptions import PermissionDenied
logger = mod_logger.get_logger(__name__)


class EventsLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR', )
        method_gp = request.META.get('REQUEST_METHOD', )
        url = request.META.get('HTTP_REFERER', )
        if ip:
            self.count += 1
        response = self.get_response(request)
        logger.info(f'url:  {url}  запрос:  {method_gp}')
        return response


class FilterIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ips = ['127.0.0.1']
        # allowed_ips = ['']
        ip = request.META.get('REMOTE_ADDR', )
        if ip not in allowed_ips:
            raise PermissionDenied
        response = self.get_response(request)
        return response


class TimeSleepIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0

    def __call__(self, request):
        if request.META.get('REMOTE_ADDR', ):
            self.count += 1
        if self.count % 2 == 0:
            response = self.get_response(request)
            return response
        else:
            time.sleep(3)
            response = self.get_response(request)
            return response














