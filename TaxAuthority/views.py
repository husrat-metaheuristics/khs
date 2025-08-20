from django.shortcuts import render,redirect
from django import forms
from KHSystemApp.models import *
from .forms import TaxAuthorityForm


# Create your views here.
def index(request):
    context={'taxauthorities':TaxAuthority.objects.all()}
    return render(request,'TaxAuthority/index.html',context)

def insert_(request,id=0):
    taxauth=TaxAuthority()
    if request.method=="GET":
        if id==0:  #id is zero for the insert operation
           form=TaxAuthorityForm()
        else:
           obj_taxauthority=TaxAuthority.objects.get(pk=id)
           form=TaxAuthorityForm(instance=obj_taxauthority)
        return render(request,'TaxAuthority/insert.html',{'form':form})
    else:
        if id==0:
           form=TaxAuthorityForm(request.POST)
        else:
            obj_taxauthority=TaxAuthority.objects.get(pk=id) 
            form=TaxAuthorityForm(request.POST,instance=obj_taxauthority)
        if form.is_valid():
            form.save()
        return redirect('/taxauthority/')

def delete_(request,id):
    tx=TaxAuthority.objects.get(pk=id)
    tx.delete() 
    return redirect("/taxauthority/")