from django.shortcuts import render,redirect
from KHSystemApp.models import SalesTaxInvoice,Invoices
from .forms import salesTaxInvoiceForm

def sales_tax_ui(request,id=0):
    if request.method=="GET":
        if id==0:
            form=salesTaxInvoiceForm()
        else:
            st=getsalestaxInv(id)
            form=salesTaxInvoiceForm(instance=st)
        return render(request,'VendorSalesTaxInvoice/sales_tax_ui.html',{'form':form}) 
    else:
        if id==0:
            form=salesTaxInvoiceForm(request.POST,request.FILES)
        else:
            st=getsalestaxInv(id)
            form=salesTaxInvoiceForm(request.POST,request.FILES,instance=st)
        if form.is_valid():
            form.save()
        return redirect('/invoices/')


def sales_tax_d(request,id):
     st=getsalestaxInv(id)
     st.delete()
     return redirect('/invoices/')
def back_to_invoices(request):
    return redirect('/invoices/')
     
def sales_tax_details(request,id):
     st=getsalestaxInv(id)
     ctx={"st":st}
     return render(request,'VendorSalesTaxInvoice/sales_tax_detail.html',ctx)

def getsalestaxInv(id):
    st=SalesTaxInvoice.objects.get(pk=id)
    return st



