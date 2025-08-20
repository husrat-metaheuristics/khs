from django.shortcuts import render,redirect
from KHSystemApp.models import *
from .forms import VendorForm

# Create your views here.

def index(request):
    context={'vendors':Vendor.objects.all()}
    return render(request,'Vendor/index.html',context)

def insert_(request,id=0):

    if request.method=="GET":
        if id==0:
            form=VendorForm()
        else:
            obj_vnd=Vendor.objects.get(pk=id)
            form=VendorForm(instance=obj_vnd)
        return render(request,'Vendor/insert.html',{'form':form})
    else:
        if id==0:
            form=VendorForm(request.POST,request.FILES)
        else:
            obj_vnd=Vendor.objects.get(pk=id)
            form=VendorForm(request.POST,instance=obj_vnd)
        if form.is_valid():
            form.save()
        return redirect('/vendor/')



def delete_(request,id):
    vendor=Vendor.objects.get(pk=id)
    vendor.delete()
    return redirect("/vendor/")

def details_(request,id):
    vendor=Vendor.objects.get(pk=id)
    return render(request,"Vendor/details.html")