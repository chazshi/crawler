from django.http import HttpResponse

def hello(request):
    return HttpResponse(u"你好")


