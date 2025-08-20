from django.shortcuts import render,redirect
from .forms import iPortalPreparationForm
from Estimate.views import *
from ReimbInvoice.views import *
from JazzReceiptNumberRequest.views import pdf_merge 
from AssembleAndExportEmail.views import *
from Estimate.utilities.resources import res
import PyPDF2
import io
from PyPDF2 import PdfFileReader, PdfFileWriter
from django.http import HttpResponse,FileResponse
from KHSystemApp.models import JazzReceiptNoRequest,Estimate,Invoices
from reportlab.platypus import Table,TableStyle,SimpleDocTemplate
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def iportal_insert(request,id=0):
    if request.method=="GET":    
        if id==0:
            form=iPortalPreparationForm()
        else:
            iportal_obj=iPortalPreparation.objects.get(pk=id)
            form=iPortalPreparationForm(instance=iportal_obj) 
        return render(request,'iPortalPreparation/iportal_ui.html',{'form':form})
    else:
        if id==0:
            form=iPortalPreparationForm(request.POST,request.FILES)
        else:
            iportal_obj=iPortalPreparation.objects.get(pk=id)
            form=iPortalPreparationForm(request.POST,request.FILES,instance=iportal_obj)
        if form.is_valid():
            form.save()
    return redirect('/invoices/')

def iportal_delete(request,id):
    iportal=getiPortalPreparation(id)
    iportal.delete()
    return redirect('/invoices/')

def iportal_details(request,id):
    return redirect('/invoices/')

def iportal_pdf(request,id):
   iportal=getiPortalPreparation(id)
   salesTaxInv=getSalesTaxInvoice(id)
   asmEmail=getAssembleEmailTxt(id)
   pdfs=[iportal.ptiPdfFile,iportal.riPdfFile,salesTaxInv.salesTaxFile,asmEmail.emailsPdfFile]
   response=pdf_merge(pdfs,id)
   return response


def getSalesTaxInvoice(id):
    return SalesTaxInvoice.objects.get(pk=id)

def getiPortalPreparation(id):
    return iPortalPreparation.objects.get(pk=id)

def file_name_iportal(id):
    inv=getInvoice(id)
    file_name=str('attachment; filename= iportal_'+inv.title+'.pdf')
    return file_name

    


