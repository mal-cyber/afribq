from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .models import main_amirs,ran
from .forms import membershipForm,ranForm
from django.contrib.auth import authenticate, login
from django.db import connection
import smtplib, ssl
# Create your views here.
def membership(request):
    if request.method == "POST":
        f = membershipForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('success')
    else:
        f = membershipForm()
        return render(request,"amirs/membership.html",{"form":f})

def success(request):
    cursor = connection.cursor()
    cursor.execute("SELECT email FROM amirs_members ORDER BY id DESC LIMIT 1")
    r = cursor.fetchone()
    port = 465  # For SSL
    password = input("Type your password and press enter: ")

    context = ssl.create_default_context()

    sender_email = "my@gmail.com"
    receiver_email = str(r)
    message = """\
    Subject: Dear member
    """
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("my@gmail.com", password)
        server.sendmail(sender_email, receiver_email, message)
    return render(request,"amirs/succes.html")

def RanNumGen(request):
    if request.method == 'POST':
        id_num = ranForm(request.POST.get('id_num'))
        user = authenticate(id_num=id_num)
        if user:
            if user.is_active:
                login(request,id_num)
                return HttpResponseRedirect(reverse('succes.html'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Your account is inactive.")
        return HttpResponseRedirect(reverse('index'))
    else:
        i = ranForm()
        return render(request, 'amirs/premiers.html', {'forms':i})
#def preiemirreq(request):
#    if request.method == 'POST':
#        first_name = request.POST.get('first_name')
#        last_name = request.POST.get('last_name')
#        reg_no = request.POST.get('reg_no')
#        user = authenticate(first_name=first_name,last_name=last_name,reg_no=reg_no)
#        if user:
#            if user.is_active:
#                login(request,user)
#                return HttpResponseRedirect(reverse('index.html'))
#
