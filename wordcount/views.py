from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def wheat(request):
    return  HttpResponse('<h1>Triticum aestivus: Ten thousand years! 1707</h1>')    
#  ttpResponse('<h1>Triticum aestivus: Ten thousand years! 1707</h1>')    

def about(request):
    return  render(request, "about.html")


def count(request):
    words = request.GET['fulltext']
    splitwords = words.split()
    counts = {}
    for w in splitwords:
        if not counts.get(w):
            counts[w]= 1
        else:
            counts[w] += 1   
    count_data = sorted(counts.items(), key= lambda x: (-x[1],))
    return  render(request, 'count.html', { 'words':splitwords, 'count':len(splitwords), 'count_data': count_data })        