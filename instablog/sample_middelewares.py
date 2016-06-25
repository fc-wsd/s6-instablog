
from django.shortcuts import render
from instablog.sample_exceptions import HelloWorldError
# from .sample_exceptions import HelloWorldError


class SampleMiddleware(object):
    def process_request(self, request):
        request.just_say = 'Lorem ipsum'
        # return 이 없으면 none이 반환된다.

    def process_exception(self, request, exc):
        if isinstance(exc, HelloWorldError):
            ctx = {
                'error': exc,
                'status': 500,
            }
            return render(request, 'error.html', ctx)