from django.shortcuts import render



def HomePage(request):
    return render(request, 'index.html')

def AboutPage(request):
    return render (request,'about.html')

