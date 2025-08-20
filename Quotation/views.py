from django.shortcuts import render,redirect
from KHSystemApp.models import Quotation,Invoices
from .forms import QuotationForm

# Create your views here.
def quo_insert(request,id=0):
    if request.method=="GET":
        if id==0:
            form=QuotationForm()
        else:
            quo=Quotation.objects.get(pk=id)
            form=QuotationForm(instance=quo)
        return render(request,'Quotation/quotation_ui.html',{'form':form}) 
    else:
        if id==0:
            form=QuotationForm(request.POST,request.FILES)
        else:
            obj_quo=Quotation.objects.get(pk=id)
            form=QuotationForm(request.POST,request.FILES,instance=obj_quo)
    if form.is_valid():
        form.save()
    return redirect('/invoices/')


def quo_delete(request,id):
     quo=Quotation.objects.get(pk=id)
     quo.delete()
     return redirect('/invoices/')
     
def quo_view(request,id):
     quo=Quotation.objects.get(pk=id)
     inv=Invoices.objects.get(pk=id)
     ctx={"quotation":quo,"invoice":inv}
     print(quo.quotationFile)
     print(quo.quotationReceivedDate)
     print(inv.title)
     return render(request,'Quotation/quotation_v.html',ctx)


