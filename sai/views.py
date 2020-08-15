from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
# Create your views here.

def Home(request):
    return render(request,'home.html')

def Aboutus(request):
    return render(request,'aboutus.html')

def Gallery(request):
    return render(request,'gallery.html')


def Sg(request):
    return render(request,'sg.html')

def Bouncers(request):
    return render(request,'bouncers.html')

def Hs(request):
    return render(request,'hs.html')


def  Sss(request):
    return render(request,'sss.html')

def Hsk(request):
    return render(request,'hsk.html')

def Ms(request):
    return render(request,'ms.html')

def Ob(request):
    return render(request,'ob.html')


def Gs(request):
    return render(request,'gs.html')



def Contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message =request.POST['message']
        send_mail(
            name ,
            'Reply me at :-'+ email + '\n' +'Message:-'+  message,
            email,
            ['anilthapa1939@gmail.com'],
            fail_silently= False
        )
        return render(request,'contactus.html',{'name':name})


    else :
        return render(request,'contactus.html')


def Gallery(request):
    return render(request,'gallery.html')