from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from vmsproject.models import TopContent, AboutText, Product, Product_Title, Exhibition, Exhibition_Title, Team, Team_Title, Testimonial, Testimonial_Title, Partner, Partner_Title, Services, Contact,Contact_info,Topbar, Navigationbar,thanks
from django.contrib import messages



def index(request):
    hometext1 = TopContent.objects.all()[0]
    hometext2 = AboutText.objects.all()[0]
    hometext3 = Product.objects.all()
    hometext4 = Exhibition.objects.all()
    hometext5 = Team.objects.all()
    hometext6 = Testimonial.objects.all()
    hometext7 = Partner.objects.all()
    hometext8 = Topbar.objects.all()[0]
    hometext9 = Navigationbar.objects.all().order_by('pos')
    hometext10 = Product_Title.objects.all()[0]
    hometext11 = Exhibition_Title.objects.all()[0]
    hometext12 = Team_Title.objects.all()[0]
    hometext13 = Testimonial_Title.objects.all()[0]
    hometext14 = Partner_Title.objects.all()[0]
    data={
        'hometext1': hometext1,
        'hometext2': hometext2,
        'hometext3': hometext3,
        'hometext4': hometext4,
        'hometext5': hometext5,
        'hometext6': hometext6,
        'hometext7': hometext7,
        'hometext8': hometext8,
        'hometext9': hometext9,
        'hometext10': hometext10,
        'hometext11': hometext11,
        'hometext12': hometext12,
        'hometext13': hometext13,
        'hometext14': hometext14,

    }
    return render(request, 'index.html', data)

def about(request):
    hometext2 = AboutText.objects.all()[0]
    hometext8 = Topbar.objects.all()[0]
    hometext9 = Navigationbar.objects.all().order_by('pos')
  
    data={
        'hometext2': hometext2,
        'hometext8': hometext8,
        'hometext9': hometext9,
    }
    # return HttpResponse("This is a about page")
    return render(request, 'about.html', data)


def service(request):
    servicetext = Services.objects.all()
    hometext8 = Topbar.objects.all()[0]
    hometext9 = Navigationbar.objects.all().order_by('pos')
    data={
        'servicetext': servicetext,
        'hometext8': hometext8,
        'hometext9': hometext9,
    }
    return render(request, 'service.html', data)

def products(request):
    hometext3 = Product.objects.all()
    hometext8 = Topbar.objects.all()[0]
    hometext9 = Navigationbar.objects.all().order_by('pos')
    data={
        'hometext3': hometext3,
        'hometext8': hometext8,
        'hometext9': hometext9,
    
    }
    return render(request, 'products.html', data)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message =request.POST['message']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(subject)<3 or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, subject=subject, message=message)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
            return HttpResponseRedirect('/thanks')

    contactinfo = Contact_info.objects.all()[0]
    hometext8 = Topbar.objects.all()[0]
    hometext9 = Navigationbar.objects.all().order_by('pos')
    data={
        'contactinfo': contactinfo,
        'hometext8': hometext8,
        'hometext9': hometext9
    }

   

    return render(request, 'contact.html', data)

def thank(request):
    hometext8 = Topbar.objects.all()[0]
    hometext9 = Navigationbar.objects.all()
    text = thanks.objects.all()[0]
    data={
        'hometext8': hometext8,
        'hometext9': hometext9,
        'text': text
    }
    
    return render(request, 'thanks.html', data)

# Create your views here.