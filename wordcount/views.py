from django.http import HttpResponse
from django.shortcuts import render
import operator

def helloworld(request):
    return HttpResponse('hello world')

def home(request):
    return render(request, 'home.html')

def count(request):
    textdisplay = request.GET['fulltext']
    wordlist = textdisplay.split()
    worddict = {}
    for word in wordlist:
        if word.lower() in worddict:
            #increase the count
            worddict[word.lower()] += 1
        # or add to dictionary
        else:
            worddict[word.lower()] = 1

    sortedWords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    # worddict.items() turns the dictionary into a list
    return render(request, 'count.html', {'fulltext': textdisplay, 'count': len(wordlist), 'sortedWords': sortedWords })

def about(request):
    return render(request, 'about.html')
