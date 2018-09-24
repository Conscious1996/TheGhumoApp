from django.shortcuts import render,redirect

from mysql import connector

# This views is of ContactApp.

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        con=connector.connect(host='localhost',user='root',password='password4723',database='touristappdb',auth_plugin='mysql_native_password')
        query=f"insert into touristcontactinfo values('{name}','{email}','{message}');"
        cursor=con.cursor()
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        return redirect('/contact')
    elif request.method=='GET':
        return render(request,'contact.html')
