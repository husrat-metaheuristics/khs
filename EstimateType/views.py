from django.shortcuts import render,redirect
from .forms import estimateTypeForm
from KHSystemApp.models import *

def estimateType_ui(request, id=0): 
    if request.method=="GET":
        if id==0:
           form=estimateTypeForm()
        else:
            obj=getEstimateType(id)
            form=estimateTypeForm(instance=obj)
        return render(request,"EstimateType/insert.html",{'form':form})
        
    else: 
        if id==0:
            form=estimateTypeForm(request.POST)
        else: 
             obj=getEstimateType(id)
             form=estimateTypeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('/invoices/')


def estimateType_idx(request):
    context1={'estimateTypes':EstimateType.objects.all() }
    return render(request,"EstimateType/index.html",context1)

def estimateType_d(request,id):
    cs1=getEstimateType(id)
    cs1.delete() 
    return redirect("/estimateType_index/")

def getEstimateType(id):
    return EstimateType.objects.get(pk=id)

