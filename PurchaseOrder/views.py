from django.shortcuts import render,redirect
from KHSystemApp.models import PurchaseOrder,Invoices
from .forms import PoForm

# Create your views here.
def po_ui(request,id=0):
    if request.method=="GET":
        if id==0:
            form=PoForm()
        else:
            po=PurchaseOrder.objects.get(pk=id)
            form=PoForm(instance=po)
        return render(request,'PurchaseOrder/po_ui.html',{'form':form}) 
    else:
        if id==0:
            form=PoForm(request.POST,request.FILES)
        else:
            obj_po=PurchaseOrder.objects.get(pk=id)
            form=PoForm(request.POST,request.FILES,instance=obj_po)
    if form.is_valid():
        form.save()
    return redirect('/invoices/')


def po_d(request,id):
     po=PurchaseOrder.objects.get(pk=id)
     po.delete()
     return redirect('/invoices/')
     
def po_preview(request,id):
     po=PurchaseOrder.objects.get(pk=id)
     inv=Invoices.objects.get(pk=id)
     ctx={"quotation":po,"invoice":inv}
     return render(request,'PurchaseOrder/po_preview.html',ctx)