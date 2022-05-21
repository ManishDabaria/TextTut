# I have create this file = Manish

from os import remove
import re
from django.http import HttpRequest, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name':'Manish', 'place':'Jaipur'}
    return render(request, 'index.html', params)


   
""" VIDEO #7 """

def analyze(request):
    # get the text
    djtext = (request.POST.get('textarea', 'default'))

    # Check Checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
    
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
            
        params = {'purpose' : 'Removepunctuation', 'analyzed_text' : analyzed}
        djtext = analyzed

        

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to Uppercase', 'analyzed_text' : analyzed}
        djtext = analyzed

        



    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            
        
        params = {'purpose' : 'Removed Newlines', 'analyzed_text' : analyzed}
        djtext = analyzed

        

    if(spaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed


        


    if(charcount == "on"):
        analyzed = 0
        
        for char in djtext:
            analyzed += 1


        params = {'purpose' : 'Total no. of character', 'analyzed_text' : analyzed}
        

    if(removepunc != "on" and newlineremover!="on" and spaceremover != "on" and fullcaps !="on" and charcount != "on"):
         return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
