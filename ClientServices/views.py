from django.shortcuts import render,redirect
from .forms import ClientServicesForm
from KHSystemApp.models import *

def insert_(request, id=0): 
    if request.method=="GET":
        if id==0:
           form=ClientServicesForm()
        else:
            obj_clientServices=ClientServices.objects.get(pk=id)
            form=ClientServicesForm(instance=obj_clientServices)
        return render(request,"ClientServices/insert.html",{'form':form})
        
    else: 
        if id==0:
            form=ClientServicesForm(request.POST)
        else: 
             obj_clientServices=ClientServices.objects.get(pk=id)
             form=ClientServicesForm(request.POST,instance=obj_clientServices)
        if form.is_valid():
            form.save()
        return redirect('/clientservices/')







def index(request):
    context1={'clientservices':ClientServices.objects.all() }
    return render(request,"ClientServices/index.html",context1)

def delete_(request,id):
    cs1=ClientServices.objects.get(pk=id)
    cs1.delete() 
    return redirect("/clientservices/")

#adjust it according to your needs.
def details_(request,id):
    cs2=ClientServices.objects.get(pk=id)
    #context2={'clientservices':cs2.invoices }
    return render(request,"ClientServices/details.html")




