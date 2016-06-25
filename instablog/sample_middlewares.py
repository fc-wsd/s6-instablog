from django.shortcuts import render
from instablog.sample_exceptions import HelloWorldError

class SampleMiddleware(object):
    def process_request(self, request): #request가 일어나는 시점에 호출 request객체에 속성추가됨
         request.just_say = 'HI'

    def process_exception(self, request, exc):
        if isinstance(exc, HelloWorldError):
            ctx={
                'error':exc,
                'status':500,
            }
            return render(request,'error.html',ctx)
