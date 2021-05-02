from django.http import HttpResponse
from django.shortcuts import render
from .models import Person,Dog

def index(request):
    return HttpResponse('Hello World')

# view using loader()
# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())  #is going to produce html and pass to HttpResponse. This requried two steps instead of 1 step which is what render does

# view using render()
def index(request):
    return render(request, 'index.html')

def listing(request):
    data = {
        "people": Person.objects.all(),
        "dogs":Dog.objects.all(),
    }

    # here we're passing the data to our template 
    # we can use tags in our template to display our data
    return render(request, "second.html",data)
