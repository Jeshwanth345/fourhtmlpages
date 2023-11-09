from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request,'page1.html')

def two(request):
    return render(request,'page2.html')

def three(request):
    return render(request,'page3.html')

def four(request):
    return render(request,'page4.html')


