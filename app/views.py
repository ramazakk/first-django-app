from django.shortcuts import render
from .models import Person

# Create your views here.

def index_view(request):
    people = Person.objects.all()
    context = {'people': people}
    return render(request, 'app/index.html', context)