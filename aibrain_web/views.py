from django.http import HttpResponse

def run_views(request):
    #request主要封装了的是请求的信息
    return HttpResponse('<h1>AIBrain DJANGO WEB</h1>')

def run1_views(request, num):
    return HttpResponse("传递的参数是:"+num)

def run2_views(request, num1, num2):
    return HttpResponse("参数１:"+num1+",参数２:"+num2)

def show_views(request, name, age):
    return HttpResponse("参数１:"+name+",参数２:"+age)
