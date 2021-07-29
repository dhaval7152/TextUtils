# created by developer -dhaval
from django.http import HttpResponse
from django.shortcuts import render


# program 6


# def index(request):
#     return HttpResponse("<h1>hello bhai</h1>")

# def about(request):
#     return HttpResponse('about us will be coming soon')
#
# def dhaval(request):
#     file=open("mysite/dhaval.txt","r")
#     f=file.readlines()
#     return HttpResponse(f)
#
#
# def insta(request):
#     return HttpResponse('''<h1>Welcome to Instagram</h1><br>
#     <input type="text" placeholder="enter the Username"><br><input type="text" placeholder="enter the Password"><br>
#     <input type="submit" value="submit">''')


# program 8

# def index(request):
#     return render(request,'index.html')

# program 10
# def capitilize(request):
#     return HttpResponse("capitilize  word")
#
# def newline(request):
#     return HttpResponse('''<h1>new line</h1>
#     <a href="http://127.0.0.1:8000/">back</a>''')
#
# def removepunc(request):
#     # get the text
#     output= request.GET.get('text','default')
#     print(output)
#     # analze the text
#     return HttpResponse('''removepunc  word `<a href="http://127.0.0.1:8000/">back</a>''')
#
# def spaceremove(request):
#     return HttpResponse('''spaceremove  word <a href="http://127.0.0.1:8000/">back</a>''')
#
# def charcount(request):
#     return HttpResponse('''charcount  word <a href="http://127.0.0.1:8000/">back</a>''')
#

# program 11

# def index(request):
#     return render(request, 'index.html')


# def analyze(request):
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     removepunc = request.GET.get('removepunc','off')
#     print(removepunc)
#     print(djtext)
#     analyzed = djtext
#     params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
#
#     return render(request,'analyze.html', params)

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
