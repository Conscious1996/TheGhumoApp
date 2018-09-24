from django.shortcuts import render

# This Views is of ServiceApp.

def service(request):
    return render(request,'services.html')
