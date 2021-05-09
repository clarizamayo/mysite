from django.http import HttpResponse
from django.shortcuts import render
from .models import Person,Dog
from django.contrib.auth.models import User
from .forms import UserForm, AdoptionForm
from .models import Adoption
# def index(request):
#     return HttpResponse('Hello World')

# view using loader()
# def index(request):
#     template = loader.get_template('index.html')
#     return HttpResponse(template.render())  #is going to produce html and pass to HttpResponse. This requried two steps instead of 1 step which is what render does

def index(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm
    return render(request, 'index.html', context={'users':users, 'form': form})

def adoption(request):
    c = Adoption.objects.all()
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AdoptionForm

    return render(request, 'contact.html', context={'contacts': c, 'form': form})

def listing(request):
    data = {
        "people": Person.objects.all(),
        "dogs":Dog.objects.all(),
    }

    # here we're passing the data to our template 
    # we can use tags in our template to display our data
    return render(request, "second.html",data)


