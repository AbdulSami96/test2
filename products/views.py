from django.http import HttpResponse
from django.shortcuts import render
from . models import Book, Fiction, NonFiction, Urdu, Child, Horror
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})
def about(request):
    return render(request, 'about.html')
def shop(request):
    fictions = Fiction.objects.all()
    Nonfictions = NonFiction.objects.all()
    Urdus = Urdu.objects.all()
    Childs = Child.objects.all()
    Horrors = Horror.objects.all()
    context = {'fictions': fictions,'NonFictions': Nonfictions, 'Urdus': Urdus, 'Childs':Childs, 'Horrors':Horrors }
    return render(request, 'shop.html', context)
def glass(request):
    return render(request, 'glass.html')
def contact(request):
    return render(request, 'contact.html')
