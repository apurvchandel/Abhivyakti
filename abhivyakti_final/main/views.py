from django.views.generic import CreateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import UpdateView
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, "index.html")


def events(request):
    return render(request, "events.html")


def contact(request):
    return render(request, "contact.html")


def Registration(request):
    if request.method == "POST":
        form = AgtForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = AgtForm()
    return render(request, 'agt.html', {'form': form, 'price' : 100})

def bigroar(request):
    if request.method == "POST":
        form = BigRoarForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = BigRoarForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})


def vyak(request):
    if request.method == "POST":
        form = vyaktitvaForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = vyaktitvaForms()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})


def antra(request):
    if request.method == "POST":
        form = AntraForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = AntraForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})


def kav(request):
    if request.method == "POST":
        form = KavyanForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = KavyanForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})


def ToTheBeat1(request):
    if request.method == "POST":
        form = ToTheBeatForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = ToTheBeatForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})


def ToTheBeatG(request):
    if request.method == "POST":
        form = ToTheBeatGForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = ToTheBeatGForm()
    return render(request, 'tothebeatg.html', {'form': form, 'price': 100})


def Talk(request):
    if request.method == "POST":
        form = TalkForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = TalkForm()
    return render(request, 'talk.html', {'form': form, 'price': 100})


def craftix(request):
    if request.method == "POST":
        form = CraftixForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = CraftixForm()
    return render(request, 'bigroar.html', {'form': form, 'price': 100})
