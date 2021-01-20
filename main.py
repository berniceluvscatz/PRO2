from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request,'base/index.html')


def Happy(request):
    category=['1']
    movie=Movies.objects.filter(category=category)
    context = {'movie':movie}
    return render(request,'base/happy.html',context)


def Average(request):
    category=['2']
    movie=Movies.objects.filter(category=category)
    context = {'movie':movie}
    return render(request,'base/happy.html',context)

def Sad(request):
    category=['3']
    movie=Movies.objects.filter(category=category)
    context = {'movie':movie}
    return render(request,'base/happy.html',context)


def Scale(request):
    res = 0
    if request.method == 'POST':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])

        res =  abs(10-(val1-val2))

    context = {'res':res}
    return render(request,'base/scale.html',context)

def Search(request):

	query = request.GET['query']
	products = Movies.objects.filter(funny_film__icontains=query)
	# sad_film = Movies.objects.filter(sad_film__icontains=query)
	# products = funny_film.union(sad_film)
	context = {'products':products}
	return render(request,'base/search.html', context)


def Search1(request):

	query = request.GET['query']

	products = Movies.objects.filter(sad_film__icontains=query)
	# products = funny_film.union(sad_film)
	context = {'products':products}
	return render(request,'base/search.html', context)


def Search2(request):

	query = request.GET['query']

	products = Movies.objects.filter(film_intense__icontains=query)
	# products = funny_film.union(sad_film)
	context = {'products':products}
	return render(request,'base/search.html', context)
