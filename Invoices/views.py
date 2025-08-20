from django.shortcuts import render,redirect
from .forms import InvoicesForm
from  KHSystemApp.models import *
import itertools
import datetime
from Estimate.views import *
from pti.views import *
from Estimate.utilities.utility import createLink,createButton 
# Create your views here.

def index(request):
    titles=['Vendor Quotation','Estimate Generation','Purchase Requsition','Purchase Order','Reimbursement Inv','Provision To Invoice','Receipt No Requested(PTI+RI+PO)','Receipt# Received(Updated PTI)','Request Sales Tax Invoice','Upload Emails Text','iPortal Uploading']    
    inserts=['quotation_i','estimate_i','pr_i','po_i','reimb_i','pti_i','jazzrecreq_i','rnr_i','sales_tax_i','asmEmail_i','iportal_i']
    edits=['quotation_u','estimate_u','pr_u','po_u','reimb_u','pti_u','jazzrecreq_u','rnr_u','sales_tax_u','asmEmail_u','iportal_u']
    deletes=['quotation_d','estimate_d','pr_d','po_d','reimb_d','pti_d','jazzrecreq_d','rnr_d','sales_tax_d','asmEmail_d','iportal_d']
    previews=['quotation_v','estimate_v','pr_preview','po_preview','reimb_v_adv','pti_v_adv','jazzrecreq_v','rnr_detail','sales_tax_det','asmEmail_details','iportal_dtls']
    allInvoicesList=[]
    invoices=Invoices.objects.all()
    outerCounter=1
    for inv in invoices:
        txtToDisplay='Some Text'
        counter=1
        isInvFullyPaid=False
        if inv.advancepayment==100:
            isInvFullyPaid=True
        statusUrls=[]
        for (title,inst,edit,dele,preview) in itertools.zip_longest(titles,inserts,edits,deletes,previews):
            txtToDisplay=' Stage Yet To Be Processed '
            doesExists=False
            hasExtraLnk=False
            hasReceiptRequestLinks=False
            haveiPortalLinks=False
            requirmentSatisfied=False
            adv_preview_lnk=' '
            rem_preview_lnk=' '
            adv_pdf_lnk=' '
            rem_pdf_lnk=' '
            if counter==1:
                if Quotation.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    Quo=Quotation.objects.get(pk=inv.id)
                    txtToDisplay=str('<br/>Date(Rec):'
                                      +str(Quo.quotationReceivedDate.strftime("%b %d, %Y"))
                                      +'<br/> Notes:-'+Quo.notes
                                      +'<br/>Vendor Quotation:'
                                      +createLink(Quo.quotationFile,'Get pdf')
                                     )                                   
            elif counter==2:
                if Estimate.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    hasExtraLnk=True      
                    est=getEstimate(inv.id)
                    
                    if isfullyPaid(inv.id):
                      adv_preview_lnk='estimate_v'
                      adv_pdf_lnk='estimates_pdf_adv'
                    else:
                      adv_preview_lnk='estimate_v'
                      adv_pdf_lnk='estimates_pdf_adv'
                      rem_preview_lnk='estimate_v_rem'
                      rem_pdf_lnk='estimates_pdf_rem'
                    txtToDisplay=str('<br/>Est Gen Date(Rec):-'
                                      +str(est.estimateGenerationDate.strftime("%b %d, %Y"))
                                      +'<br/>Est Shared Date(Rec):-'
                                      +str(est.sharedToClientDate.strftime("%b %d, %Y"))
                                      +'<br/> Notes:-'+est.notes+'<br/>'                                                           
                                     )                   
            elif counter==3:
                if PurchaseRequsition.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    pr=PurchaseRequsition.objects.get(pk=inv.id)
                    txtToDisplay=str('<br/>Requested Date:-'
                                      +str(pr.prRequestedDate.strftime("%b %d, %Y"))+'<br/>'
                                      +'Received Date:-'
                                      +str(pr.prReceivedDate.strftime("%b %d, %Y"))+'<br/>'
                                      +'PR Number:- '
                                      +str(pr.prNumber)+'<br/>'
                                      +'Notes:-'+pr.notes+'<br/>'                                                           
                                    ) 
            elif counter==4:
                if PurchaseOrder.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    po=PurchaseOrder.objects.get(pk=inv.id)
                    txtToDisplay=str('<br/>Requested Date:-'
                                      +str(po.poRequestedDate.strftime("%b %d, %Y"))+'<br/>'
                                      +'Received Date:-'
                                      +str(po.poReceivedDate.strftime("%b %d, %Y"))+'<br/>'
                                      +'PO Number:- '
                                      +str(po.poNumber)+'<br/>'
                                      +'Notes:-'+pr.notes+'<br/>'
                                      +'PO File:-'
                                      +createLink(po.poFile,'Get pdf')                                                           
                                    ) 
            elif counter==5:
                if Reimbursement.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    hasExtraLnk=True      
                    reimb=getReimbursementInv(inv.id) 
                    if isfullyPaid(inv.id):
                      adv_preview_lnk='reimb_v_adv'
                      adv_pdf_lnk='reimb_pdf_adv'
                    else:
                      adv_preview_lnk='reimb_v_adv'
                      adv_pdf_lnk='reimb_pdf_adv'
                      rem_preview_lnk='reimb_v_rem'
                      rem_pdf_lnk='reimb_pdf_rem'
                    txtToDisplay=str('<br/>RI Number:-'
                                      +str(reimb.reInvNumber)
                                      +'<br/>RI Inv Date:-'
                                      +str(reimb.reInvDate.strftime("%b %d, %Y"))
                                      +'<br/> Notes:-'+reimb.notes+'<br/>'
                                    )   
            elif counter==6:
                if Pti.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    hasExtraLnk=True      
                    pti=getPti(inv.id) 
                    if isfullyPaid(inv.id):
                      adv_preview_lnk='pti_v_adv'
                      adv_pdf_lnk='pti_pdf_adv'
                    else:
                      adv_preview_lnk='pti_v_adv'
                      adv_pdf_lnk='pti_pdf_adv'
                      rem_preview_lnk='pti_v_rem'
                      rem_pdf_lnk='pti_pdf_rem'
                    txtToDisplay=str('<br/>PTI Date:-'
                                      +str(pti.ptiDate.strftime("%b %d, %Y"))
                                      +'<br/> Notes:-'+pti.notes+'<br/>'
                                    )  
            elif counter==7:
                hasReceiptRequestLinks=True
                if JazzReceiptNoRequest.objects.filter(pk=inv.id).count()==0:
                    doesExists=False                   
                else:
                    doesExists=True
                    recReq=JazzReceiptNoRequest.objects.get(pk=inv.id)
                    txt_updation=' '
                    if PurchaseOrder.objects.filter(pk=inv.id).count()>0 and JazzReceiptNoRequest.objects.filter(pk=inv.id).count()>0:
                        po__=PurchaseOrder.objects.get(pk=inv.id)
                        if len(str(recReq.advRiFile))>0 and len(str(recReq.initialPtiFile))>0 and len(str(po__.poFile))>0:
                            requirmentSatisfied=True
                        else:
                            txt_updation='Receipt Request Requirements Not Fullfilled'
                    else:
                        txt_updation='Receipt Request Requirements Not Fullfilled'                                                                 
                    txtToDisplay=str('<br/>Date Requested:-'
                                      +str(recReq.receiptReqDate.strftime("%b %d, %Y"))
                                      +'<br/> Notes:-'+recReq.notes+'<br/>'
                                      +'<br/>'+txt_updation+'<br/>'
                                    )
            elif counter==8:
                if ReceiptNumberReceived.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    hasExtraLnk=True      
                    rn=getReceiptNumber(inv.id)
                    if isfullyPaid(inv.id):
                      adv_preview_lnk='pti_v_adv'
                      adv_pdf_lnk='pti_pdf_adv'
                    else:
                      adv_preview_lnk='pti_v_adv'
                      adv_pdf_lnk='pti_pdf_adv'
                      rem_preview_lnk='pti_v_rem'
                      rem_pdf_lnk='pti_pdf_rem'
                    txtToDisplay=str('<br/>Receipt(Rec) Date:-'
                                      +str(rn.receiptReceivedDate.strftime("%b %d, %Y"))
                                      +'<br/>Receipt #:-'
                                      +str(rn.receiptNumber)
                                      +'<br/> Notes:-'+rn.notes+'<br/>'
                                    )  
            elif counter==9:
                if SalesTaxInvoice.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    sal_tax=SalesTaxInvoice.objects.get(pk=inv.id)
                    txtToDisplay=str('<br/>Sale Tax Date(Req):'
                                      +str(sal_tax.salesTaxInvoiceRequestedDate.strftime("%b %d, %Y"))
                                      +'<br/>Sale Tax Date(Rec):'
                                      +str(sal_tax.salesTaxInvoiceReceivedDate.strftime("%b %d, %Y"))
                                      +'<br/> Notes:-'+sal_tax.notes
                                      +'<br/>Sale Tax Invoice:'
                                      +createLink(sal_tax.salesTaxFile,'Get pdf')
                                     ) 
            elif counter==10:
                if AssembleExportEmail.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    txtToDisplay='----'
            elif counter==11:
                haveiPortalLinks=True
                if iPortalPreparation.objects.filter(pk=inv.id).count()==0:
                    doesExists=False
                else:
                    doesExists=True
                    iportal=iPortalPreparation.objects.get(pk=inv.id)
                    txt_updation=' '
                    if iPortalPreparation.objects.filter(pk=inv.id).count()>0 and AssembleExportEmail.objects.filter(pk=inv.id).count()>0 and SalesTaxInvoice.objects.filter(pk=inv.id).count()>0:
                       asmEx=AssembleExportEmail.objects.get(pk=inv.id)
                       salTax=SalesTaxInvoice.objects.get(pk=inv.id)      
                       if len(str(iportal.ptiPdfFile))>0 and len(str(iportal.riPdfFile))>0 and len(str(asmEx.emailsPdfFile))>0 and len(str(salTax.salesTaxFile))>0:
                            requirmentSatisfied=True
                            txtToDisplay=str('<br/>iPortal Uploaded Date:-'
                                      +str(iportal.uploadedDate.strftime("%b %d, %Y"))
                                      +'<br/> Notes:-'+iportal.notes+'<br/>'
                                      +'<br/> PTI:-'
                                      +createLink(iportal.ptiPdfFile,'Get PDF')
                                      +'<br/> RI:-'
                                      +createLink(iportal.riPdfFile,'Get PDF')
                                      +'<br/> Email:-'
                                      +createLink(asmEx.emailsPdfFile,'Get PDF')
                                      +'<br/> Sales Tax:-'
                                      +createLink(salTax.salesTaxFile,'Get PDF')                                     
                                    )
                       else:
                           txt_updation='iPortal Requirements Not Fullfilled File Missing'
                           txtToDisplay=txt_updation
                    else:
                           txt_updation='iPortal Requirements Not Fullfilled.Object Not Created Yet'
                           txtToDisplay=txt_updation
    

            link=statusLinks(isfullyPaid(inv.id)
                             ,hasExtraLnk
                             ,txtToDisplay
                             ,counter
                             ,title
                             ,inst
                             ,edit
                             ,dele
                             ,preview
                             ,doesExists
                             ,adv_preview_lnk
                             ,rem_preview_lnk
                             ,adv_pdf_lnk
                             ,rem_pdf_lnk
                             ,hasReceiptRequestLinks
                             ,requirmentSatisfied
                             ,haveiPortalLinks                          
                            )
            statusUrls.append(link)
            counter=counter+1

        headingId=str('heading'+str(outerCounter))
        collapseId=str('collapse'+str(outerCounter))
        collapseTarget=str('#collapse'+str(outerCounter))
        upperLnk=upperLinks(outerCounter,inv.title,inv.id,statusUrls,headingId,collapseId,collapseTarget,inv.fishbowlid)
        allInvoicesList.append(upperLnk)
        outerCounter=outerCounter+1 

    ctx={'invoices__':allInvoicesList}
    return render(request,"Invoices/index.html",ctx)

def insert_(request,id=0):
    if request.method=="GET":
        if id==0:
           form=InvoicesForm()
        else:
            obj_invoices=Invoices.objects.get(pk=id)
            form=InvoicesForm(instance=obj_invoices)
        return render(request,"Invoices/insert.html",{'form':form})
        
    else: 
        if id==0:
            form=InvoicesForm(request.POST)
        else: 
             obj_invoices=Invoices.objects.get(pk=id)
             form=InvoicesForm(request.POST,instance=obj_invoices)
        if form.is_valid():
            form.save()
        return redirect('/invoices/')
    
def delete_(request,id):
    invc=Invoices.objects.get(pk=id)
    invc.delete()
    return redirect('/invoices/')

def details_(request,id):
    invc=Invoices.objects.get(pk=id)
    ctx={'invoice':invc}
    return render(request,"Invoices/details.html",ctx)

def getEstimate(id):
    return Estimate.objects.get(pk=id)

def getPti(id):
    pti=Pti.objects.get(pk=id)
    return pti

class statusLinks:
    def __init__(self,isFullyPaidEst,hasExtraLinks,txtTodisplay
                ,counter__,title,addLink,editLink,deleteLink
                ,previewLink,isCreated, adv_preview_lnk
                ,rem_preview_lnk,adv_pdf_lnk,rem_pdf_lnk
                ,hasReceiptRequestLinks,requirmentSatisfied
                ,hasiportalLinks):
        self.isFullyPaidEst=isFullyPaidEst
        self.hasExtraLinks=hasExtraLinks
        self.txtTodisplay=txtTodisplay
        self.counter__=counter__
        self.title=title
        self.addLink=addLink
        self.editLink=editLink
        self.deleteLink=deleteLink
        self.previewLink=previewLink
        self.isCreated=isCreated
        self.adv_preview_lnk=adv_preview_lnk
        self.rem_preview_lnk=rem_preview_lnk
        self.adv_pdf_lnk=adv_pdf_lnk
        self.rem_pdf_lnk=rem_pdf_lnk
        self.hasReceiptRequestLinks=hasReceiptRequestLinks
        self.requirmentSatisfied=requirmentSatisfied
        self.hasiportalLinks=hasiportalLinks
        #self.hasFinalUploadingLinks=hasFinalUploadingLinks

class upperLinks:
    def __init__(self,outerCount,ttl,id__,stages,headingId,collapseId,collapseTarget,fishbowlid):
        self.outerCount=outerCount
        self.ttl=ttl
        self.id__=id__
        self.stages=stages
        self.headingId=headingId
        self.collapseId=collapseId
        self.collapseTarget=collapseTarget
        self.fishbowlid=fishbowlid 

def getReimbursementInv(id):
    reimb=Reimbursement.objects.get(pk=id)
    return reimb

  


