from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse('Hello World')

# view using loader()
# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())  #is going to produce html and pass to HttpResponse. This requried two steps instead of 1 step which is what render does

# view using render()
def index(request):
    return render(request, 'base.html')

def second(request):
    return render(request, 'index.html')
