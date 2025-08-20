from django.shortcuts import render,redirect
from KHSystemApp.models import *
from . import views
import itertools
import io
from .forms import reimbursementForm
from Estimate.utilities.resources import res
from Estimate.utilities.styles import *
from Estimate.utilities.fonts import *
from Estimate.utilities.utility import *
from Estimate.views import *
from django.http import HttpResponse,FileResponse
from Invoices.views import *
#from KHSystemApp.generic import EstimateDisplay,prepare

def reimb_insert(request,id=0):
    if request.method=="GET":
        if id==0:
            form=reimbursementForm()
        else:
            reimb_obj=Reimbursement.objects.get(pk=id)
            form=reimbursementForm(instance=reimb_obj)
        return render(request,'ReimbInvoice/reimb_ui.html',{'form':form})
    else:
        if id==0:
            form=reimbursementForm(request.POST)
        else:
            reimb_obj=Reimbursement.objects.get(pk=id)
            form=reimbursementForm(request.POST,instance=reimb_obj)
    if form.is_valid():
       form.save()
    return redirect('/invoices/')
     
def reimb_delete(request,id):
    reimb=Reimbursement.objects.get(pk=id)
    reimb.delete()
    return redirect('/invoices/')

def reimb_preview_rem(request,id):
  reimbDtls=previewReimbDtls(id,False)
  est=getEstimate(id)
  ctx={'values':reimbDtls.ri_list,'details':reimbDtls.detail,'ri_id':est.invoice.id,'ri_details':reimbDtls.ri_final}
  return render(request,"ReimbInvoice/reimb_inv_preview.html",ctx)

def reimb_preview_adv(request,id):
  reimbDtls=previewReimbDtls(id,True)
  est=getEstimate(id)
  ctx={'values':reimbDtls.ri_list,'details':reimbDtls.detail,'ri_id':est.invoice.id,'ri_details':reimbDtls.ri_final}
  return render(request,"ReimbInvoice/reimb_inv_preview.html",ctx)

def previewReimbDtls(id,isAdv):
  est=getEstimate(id)
  txauthy=getTaxAuthority(est.invoice.taxauthority.id)
  inv=getInvoice(id)
   
  display_ri=[]
  display_ri=estimate_display_calculation(id,True)
   ##calculations.
  proj_cost=round(amount_calculation(est.amount))
  discount__=round(discount_offered(proj_cost,inv.discountOffered))
  amt=proj_cost-discount__
  total_tax=0.0
  tax_auth_dis=' '

  if isTaxableEstimate(id):
    tax_auth_dis=str(est.invoice.taxauthority.taxauthority)
    total_tax=sales_tax(amt,est.invoice.taxauthority.taxrate)
  else:
    tax_auth_dis=' '
    total_tax=0.0
  total_cost=amt+total_tax
  detail=invoice_details(id,round(total_cost))
  note_text=' '
  if isfullyPaid(id):
    note_text=' '
  else:
    if isReimbursedEstimate(id):
      if isAdv:
        note_text=adv_line(inv.advancepayment,amt,total_tax,tax_auth_dis,False)
      else:
        note_text=rem_line(inv.advancepayment,amt,total_tax,tax_auth_dis,False)  
    else:
      if isAdv:
        note_text=adv_line(inv.advancepayment,total_cost,total_tax,tax_auth_dis,False)
      else:
        note_text=rem_line(inv.advancepayment,total_cost,total_tax,tax_auth_dis,False)         
  ri_final=estimateDisplayDetails(round(discount__)
                                 ,str('Discount('+str(round(inv.discountOffered))+'%)')
                                 ,note_text
                                 ,round(amt)
                                 ,round(total_tax)
                                 ,tax_auth_dis
                                 ,round(total_cost))
  reimbDetails=reimbursementDisplay(display_ri,detail,ri_final)
  return reimbDetails

def invoice_details(id,amtinwords):
  inv=getInvoice(id)
  reimb_inv=getReimbursemeent(id)
  po=getPurchaseOrder(id)
  amtwords=str(num2words(amtinwords)+' Rupees Only--')
  inv_detail=InvoiceDetails(inv.title,
                            reimb_inv.reInvNumber,
                            reimb_inv.reInvDate,
                            inv.fishbowlid,
                            po.poNumber,
                            po.poReceivedDate,
                            amtwords)
  return inv_detail

def getReimbursemeent(id):
  return Reimbursement.objects.get(pk=id)

def getPurchaseOrder(id):
  return PurchaseOrder.objects.get(pk=id)

def flow_obj_ri_display(id,isAdv):
  pdfmetrics.registerFont(TTFont('MainFont', 'static\_fonts\BOD_R.TTF'))
  flow_obj=[]
  est=getEstimate(id)
  inv=getInvoice(id)
  proj_cost=round(amount_calculation(est.amount))
  discount__=round(discount_offered(proj_cost,inv.discountOffered))
  amt=proj_cost-discount__
  total_tax=0.0
  tax_auth_dis=' '
  if isTaxableEstimate(id):
    tax_auth_dis=str(est.invoice.taxauthority.taxauthority+'('+str(est.invoice.taxauthority.taxrate)+'%)')
    total_tax=sales_tax(amt,est.invoice.taxauthority.taxrate)
  else:
    tax_auth_dis=' '
    total_tax=0.0
  total_cost=amt+total_tax
  detail=invoice_details(id,round(total_cost))
  txt_reimb_heading=Paragraph('''<para align=center><b>Reimbursement Invoice</b></para>''')
  checkby_data=[
                [[txt_reimb_heading],[],[],[]],
                ['FB Invoice#',str(detail.fb_inv_no),'Inv Date:',str(detail.inv_date)],
                ['Estimate#',str(detail.fb_est_no),'Client PO:',str(detail.po)],
                ['Client PO Date:',str(detail.po_date)],
               ]
  tbl_checkedBy=Table(checkby_data)
  tbl_checkedBy_style=TableStyle([
                                   ('GRID',(0,0),(-1,-1),0.7,colors.black),
                                   ('SPAN',(0,0),(-1,-4)),
                                   ('LINEABOVE',(0,1),(-1,-3),0.7,colors.black),
                                   ('FONTSIZE',(0,0),(-1,-1),8), 
                                   ('ALIGN',(0,0),(-1,-4),'CENTER')                           
                                 ])
  tbl_checkedBy.setStyle(tbl_checkedBy_style)
   
  header_data=[
                [[[logo_stamp_fishbowl(res.FISHBOWL_LOGO_PATH)],[res.REIMBURSEMENT_ADDRESS]],tbl_checkedBy],
                [str('Title:'+detail.title),[]]
              ]
  tbl_header=Table(header_data,colWidths=[280,270])
  flow_obj.append(tbl_header)
  ##Main display table for Estimate,Reimb
  estimate_main_data=main_estimate_data(id,inv.discountOffered,discount__,True)
  note_text=' '
  if isfullyPaid(id):
    note_text=' '
  else:
    if isReimbursedEstimate(id):
      if isAdv:
        note_text=adv_line(inv.advancepayment,amt,total_tax,tax_auth_dis,True)
      else:
        note_text=rem_line(inv.advancepayment,amt,total_tax,tax_auth_dis,True)  
    else:
      if isAdv:
        note_text=adv_line(inv.advancepayment,total_cost,total_tax,tax_auth_dis,True)
      else:
        note_text=rem_line(inv.advancepayment,total_cost,total_tax,tax_auth_dis,True) 
  estimate_main_data.append([' ',note_text,' ',' ',' ',' '])
  flow_obj.append(main_display_table(estimate_main_data))

  flow_obj.append(total_cal_section(proj_cost,discount__,tax_auth_dis,total_tax,False,not isAdv,inv.advancepayment,est.invoice.taxauthority.isReimbursed))

  flow_obj.append(amount_in_words(detail.amountInWords))
  flow_obj.append(company_rules(res.TXT_REIMBURSEMENT_SPECIFIC))
  flow_obj.append(company_address())
  return flow_obj

def ri_pdf_adv(request,id):
  response=get_ri_pdf(id,True)
  return response

def ri_pdf_rem(request,id):
  response=get_ri_pdf(id,False)
  return response

def get_ri_pdf(id,isAdv):
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = file_name_ri(id)
   pdf=SimpleDocTemplate(response)
   flow_obj=flow_obj_ri_display(id,isAdv)
   pdf.build(flow_obj)
   return response

def file_name_ri(id):
  inv=getInvoice(id)
  nm=str('attachment; filename='+'ri_'+inv.title+'.pdf')
  return nm

class InvoiceDetails:
  def __init__(self,title,fb_inv_no,inv_date,fb_est_no,po,po_date,amountInWords):
    self.title=title
    self.fb_inv_no=fb_inv_no
    self.inv_date=inv_date
    self.fb_est_no=fb_est_no
    self.po=po
    self.po_date=po_date
    self.amountInWords=amountInWords

class reimbursementDisplay:
  def __init__(self,ri_list,detail,ri_final):
    self.ri_list=ri_list
    self.detail=detail
    self.ri_final=ri_final


