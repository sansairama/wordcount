from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, 'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordcount=fulltext.split()
    worddict={}
    for word in wordcount:
        if word not in worddict:
            worddict[word]=1
        else:
            worddict[word]+=1
    return render(request,'count.html', {'fulltext':fulltext,'worddict':worddict})
def about(request):
    return render(request,'about.html')
