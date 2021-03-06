from django.http import HttpResponse
from django.shortcuts import render
from .models import Person,Dog
from django.contrib.auth.models import User
from .forms import UserForm, AdoptionForm
from .models import Adoption
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral6
from .chart import chart_func
from .wwii import wwii_func

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


def chartpath(request):
    p = chart_func()
    script, div = components(p)

    return render(request,'chart.html',{'script':script, 'div':div})


def wwii(request):
    p = wwii_func()
    script, div = components(p)

    return render(request,'chart_2.html',{'script':script, 'div':div})