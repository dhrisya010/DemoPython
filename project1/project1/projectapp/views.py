from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

#def prgdemo(request):
  #  return HttpResponse("HELLO PYTHON, HERE THE HOME PAGE")

#def about(request):
 #   return render(request,"ABOUT.html")

#def contact(request):
 #   return render(request,"CONTACT.html")

#def detail(request):
 #   return render(request,"detail.html")

#def thanks(request):
 #   return HttpResponse("*********HERE THE LAST PAGE*********")


#def addition(request):
 #   x=int(request.GET["num1"])
  #  y=int(request.GET["num2"])
   # result1=x+y
    #result2=x-y
    #result3=x*y
    #result4=x/y
    #return render(request,"result.html",{'res1':result1,'res2':result2,'res3':result3,'res4':result4})


