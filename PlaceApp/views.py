from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# This is the View of PlaceApp

def place(request):
    return render(request,'places\\place.html')

def detail(request):

    if request.method=="POST":

        searchedValue=request.POST.get('Searching')
        tempList=searchedValue.split(" ")
        finalValue=""
        checker=1
        lenList=len(tempList)
        for i in tempList:
            if lenList==checker:
                finalValue=finalValue+i.title()
            elif i=="":
                checker+=1
                pass
            else:
                finalValue=finalValue+i.title()+"_"
                checker+=1

        obj=requests.get(f"https://en.wikipedia.org/wiki/{finalValue}").text
        bsObj=BeautifulSoup(obj,"html.parser")
        greatList=[]
        for k in bsObj.find_all('p'):
            greatList.append(k.text)
        greatString=greatList[0]+" "+greatList[1]+" "+greatList[2]

        return render(request,'places\\detail.html',{"place":greatString})
    elif request.method=="GET":

        return render(request,'places\\detail.html',{"place":"detail of your place will be here"})
