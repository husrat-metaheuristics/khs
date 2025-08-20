from django.shortcuts import render,redirect
from KHSystemApp.models import AssembleExportEmail
from .forms import AssembleExportEmailForm
from django.http import HttpResponse
from reportlab.platypus import Paragraph,Table,TableStyle,SimpleDocTemplate
def assembleEmail_delete(request,id):
    asmTxt=getAssembleEmailTxt(id)
    asmTxt.delete()
    return redirect('/invoices/')

def getAssembleEmailTxt(id):
    asmTxt=AssembleExportEmail.objects.get(pk=id)
    return asmTxt

def assembleEmail_details(request,id):
    return redirect('/invoices/')

def assembleEmail_insert(request,id=0):
    if request.method=="GET":
        if id==0:
            form=AssembleExportEmailForm()
        else:
            asmTxt=getAssembleEmailTxt(id)
            form=AssembleExportEmailForm(instance=asmTxt)
        return render(request,'AssembleAndExportEmail/assembleEmail_ui.html',{'form':form})
    else:
        if id==0:
            form=AssembleExportEmailForm(request.POST,request.FILES)
        else:
            asm_txt=getAssembleEmailTxt(id)
            form=AssembleExportEmailForm(request.POST,request.FILES,instance=asm_txt)
    if form.is_valid():
        form.save()
    return redirect('/invoices/')