from django.shortcuts import render,redirect
from .forms import JazzReceiptReqForm
from Estimate.views import *
from ReimbInvoice.views import *
from Estimate.utilities.resources import res
import PyPDF2
import io
from PyPDF2 import PdfFileReader, PdfFileWriter
from django.http import HttpResponse,FileResponse
from KHSystemApp.models import JazzReceiptNoRequest,Estimate,Invoices
from reportlab.platypus import Table,TableStyle,SimpleDocTemplate
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def insert_(request,id=0):
    if request.method=="GET":    
        if id==0:
            form=JazzReceiptReqForm()
        else:
            jr_obj=JazzReceiptNoRequest.objects.get(pk=id)
            form=JazzReceiptReqForm(instance=jr_obj) 
        return render(request,'JazzReceiptNumberRequest/jr_ui.html',{'form':form})
    else:
        if id==0:
            form=JazzReceiptReqForm(request.POST,request.FILES)
        else:
            jr_obj=JazzReceiptNoRequest.objects.get(pk=id)
            form=JazzReceiptReqForm(request.POST,request.FILES,instance=jr_obj)
        if form.is_valid():
            form.save()
    return redirect('/invoices/')

def delete_(request,id):
    jr=JazzReceiptNoRequest.objects.get(pk=id)
    jr.delete()
    return redirect('/invoices/')

def details_(request,id):
    return redirect('/invoices/')

def pdf_(request,id):
   po=getPurchaseOrder(id)
   recReq=getJazzReceiptRequest(id)
   pdfs=[recReq.initialPtiFile,recReq.advRiFile,po.poFile]
   response=pdf_merge(pdfs,id)
   return response

def pdf_merge(pdfs,id):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = file_name_recReq(id)
    pdf_writer = PdfFileWriter()
    for pdf in pdfs:
        pdf_reader = PdfFileReader(pdf)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    outputstream=io.BytesIO()
    pdf_writer.write(outputstream)
    response.write(outputstream.getvalue())
    return response


def getJazzReceiptRequest(id):
    return JazzReceiptNoRequest.objects.get(pk=id)

def file_name_recReq(id):
    inv=getInvoice(id)
    file_name=str('attachment; filename= JazzReceiptReq_'+inv.title+'.pdf')
    return file_name

    

