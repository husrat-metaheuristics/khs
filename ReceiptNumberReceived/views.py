from django.shortcuts import render,redirect
from KHSystemApp.models import *
from ReceiptNumberReceived.forms import *

def rnr_insert_(request,id=0):
    if request.method=="GET":
        if id==0:
            form=ReceiptNumberReceivedForm()
        else:
            rnr_obj=get_receipt_no_receive(id)
            form=ReceiptNumberReceivedForm(instance=rnr_obj)
        return render(request,'ReceiptNumberReceived/rnr_ui.html',{'form':form})
    else:
        if id==0:
            form=ReceiptNumberReceivedForm(request.POST)
        else:
            rnr_obj=get_receipt_no_receive(id)
            form=ReceiptNumberReceivedForm(request.POST,instance=rnr_obj)
        if form.is_valid():
           form.save()
    return redirect('/invoices/')
     
def rnr_delete_(request,id):
    rnr=get_receipt_no_receive(id)
    rnr.delete()
    return redirect('/invoices/')
     
def rnr_detail_(request,id):
    rnr=get_receipt_no_receive(id)
    inv=Invoices.objects.get(pk=id)
    ctx={"rnr":rnr,"title":inv.title,'inv_id':inv.id}
    return render(request,'ReceiptNumberReceived/rnr_detail.html',ctx)

def get_receipt_no_receive(id):
    rnr=ReceiptNumberReceived.objects.get(pk=id)
    return rnr

def pti_with_receiptnumber(request,id):
    rnr=get_receipt_no_receive(id)
    return redirect('/invoices/')
