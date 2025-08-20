from django.shortcuts import render,redirect
from KHSystemApp.models import *
from . import views
from .forms import PrForm

def pr_ui(request,id=0):
    if request.method=="GET":
        if id==0:
            form=PrForm()
        else:
            pr_obj=PurchaseRequsition.objects.get(pk=id)
            form=PrForm(instance=pr_obj)
        return render(request,'PurchaseRequsition/pr_ui.html',{'form':form})
    else:
        if id==0:
            form=PrForm(request.POST)
        else:
            pr_obj=PurchaseRequsition.objects.get(pk=id)
            form=PrForm(request.POST,instance=pr_obj)
    if form.is_valid():
       form.save()
    return redirect('/invoices/')
     
def pr_d(request,id):
    pr=PurchaseRequsition.objects.get(pk=id)
    pr.delete()
    return redirect('/invoices/')
     
def pr_preview(request,id):
    pr=PurchaseRequsition.objects.get(pk=id)
    inv=Invoices.objects.get(pk=id)
    ctx={"pr":pr,"invoice":inv}
    return render(request,'PurchaseRequsition/pr_preview.html',ctx)


     

