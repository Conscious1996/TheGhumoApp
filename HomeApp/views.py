from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index/index.html')
def about(request):
    return render(request,'about.html')
def exp(request):
    return render(request,'index/newsexpressed.html')
