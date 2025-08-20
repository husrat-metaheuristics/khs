from django.shortcuts import render,redirect
from KHSystemApp.models import PurchaseOrder,Reimbursement,Pti,Invoices
from .forms import PtiForm
from Estimate.views import *
from datetime import date
from reportlab.lib import colors
from ReimbInvoice.views import *
from django.http import HttpResponse,FileResponse
from Estimate.utilities.resources import res
from Estimate.utilities.utility import *
from reportlab.platypus import Table,TableStyle,Paragraph,Image,SimpleDocTemplate
# Create your views here.
def pti_insert(request,id=0):
    form=''
    if request.method=="GET":
        if id==0:
            form=PtiForm()
        else:
            pti=Pti.objects.get(pk=id)
            form=PtiForm(instance=pti)
        return render(request,'Pti/pti_ui.html',{'form':form}) 
    else:
        if id==0:
            form=PtiForm(request.POST)
            print('initial Post')   
        else:
            obj_pti=Pti.objects.get(pk=id)
            form=PtiForm(request.POST,instance=obj_pti)
        if form.is_valid():
           form.save()
           print('Saved-----')
    return redirect('/invoices/')

def pti_delete(request,id):
     pti=Pti.objects.get(pk=id)
     pti.delete()
     return redirect('/invoices/')
    
def pti_preview_adv(request,id):
    rn=receiptNumberCheck(id)
    pti_preview=centralDataForPti(id,True,rn)
    ctx={'pti':pti_preview}
    return render(request,'Pti/pti_preview.html',ctx)

def pti_preview_rem(request,id):
    rn=receiptNumberCheck(id)
    pti_preview=centralDataForPti(id,False,rn)
    ctx={'pti':pti_preview}
    return render(request,'Pti/pti_preview.html',ctx)

def receiptNumberCheck(id):
    num=' '
    if ReceiptNumberReceived.objects.filter(pk=id).count()==0:
        num=' '
    else:
       rn=getReceiptNumber(id)
       num=rn.receiptNumber
    return num

def centralDataForPti(id,isAdv,receiptNumber):
  est=getEstimate(id)
  inv=getInvoice(id)
  txt_adv_rem=' '
  deduction_res=' '
  proj_cost=round(amount_calculation(est.amount))
  discount__=round(discount_offered(proj_cost,inv.discountOffered))
  amt=proj_cost-discount__
  total_tax=0.0
  total_cost=0.0

  if isTaxableEstimate(id):
      #total_tax=sales_tax(amt,est.invoice.taxauthority.taxrate)
      if isfullyPaid(id):
          #if isReimbursedEstimate(id):
              #total_cost=amt
          #else: 
              #total_cost=amt+total_tax
            total_cost=amt
      else:
           advPercentage=inv.advancepayment
           if isAdv:
              #if isReimbursedEstimate(id):
                  #total_cost=(advPercentage/100.0)*amt
              #else: 
                  #total_cost=(advPercentage/100.0)*(amt+total_tax)
              total_cost=(advPercentage/100.0)*amt
              txt_adv_rem=str(str(round(advPercentage))+'% Advance Payment')
           else:
              rem_percentage=100-advPercentage
              #if isReimbursedEstimate(id):
                  #total_cost=(rem_percentage/100.0)*amt
              #else: 
                  #total_cost=(rem_percentage/100.0)*(amt+total_tax)
              deduction_res=str(str(advPercentage)+'% Advance Received')
              total_cost=(rem_percentage/100.0)*amt
              txt_adv_rem=str(str(round(rem_percentage))+'% Balance Payment')             
  else:
      total_cost=amt
      txt_adv_rem=''

  txt_adv_rem=str((point_comma_adjustments(total_cost))+'<br/>'+txt_adv_rem)      
  po=getPoNumber(id)
  reimb=getReimbursemeent(id)
  pti_Representation=ptiRepresentation(1
                                      ,po.poNumber
                                      ,txt_adv_rem
                                      ,reimb.reInvNumber
                                      ,txt_adv_rem
                                      ,'Nil'
                                      ,txt_adv_rem
                                      ,receiptNumber
                                      ,deduction_res
                                    )
  return pti_Representation

def getReceiptNumber(id):
    rn=ReceiptNumberReceived.objects.get(pk=id)
    return rn    

def getPoNumber(id):
    po=PurchaseOrder.objects.get(pk=id)
    return po
    
def pti_pdf_rem(request,id):
    rn=receiptNumberCheck(id)
    response=get_pdf_pti(id,False,rn)
    return response

def pti_pdf_adv(request,id):
    rn=receiptNumberCheck(id)
    response=get_pdf_pti(id,True,rn)
    return response

def get_pdf_pti(id,isAdv,receiptNumber):
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = file_name_pti(id)
   pdf=SimpleDocTemplate(response)
   flow_obj=flow_obj_pti_display(id,isAdv,receiptNumber)
   pdf.build(flow_obj)
   return response

def para_txt(txt):
    para=Paragraph('''<para><font size=7>'''+txt+'''</font></para>''')
    return para

def para_txt_center(txt):
    para=Paragraph('''<para align=center><font size=10>'''+txt+'''<br/></font></para>''')
    return para

def get_table(tbl_data,isGridStyle):
    tbl=Table(tbl_data)
    if isGridStyle:
         tbl_style=TableStyle([('GRID',(0,0),(-1,-1),0.5,colors.black),
                               ('ALIGN',(0,0),(-1,-4),'CENTER'),                           
                             ])
         tbl.setStyle(tbl_style)
    return tbl

def flow_obj_pti_display(id,isAdv,receiptNumber):
    po=getPurchaseOrder(id)
    flow_obj=[]
    ##Logo Section.
    logo_section_data=[
                       [[para_txt('<b>Pakistan Mobile Communications Ltd.</b>')],[],[logo_stamp_fishbowl(res.JAZZ_LOGO_PATH)]],
                      ]
    tbl=get_table(logo_section_data,False)
    flow_obj.append(tbl)
    flow_obj.append(para_txt_center('<br/><b>Permission to Invoice</b><br/>'))
    ##Header Data Section
    header_data_section=[
                         [para_txt('Department:'),para_txt('''<u>Marketing</u>'''),para_txt('Agreement/ PO No:'),para_txt(str(po.poNumber))],
                         [para_txt('Location:'),para_txt('''<u>Islamabad</u>'''),para_txt('Contactor Name:'),para_txt('Fish Bowl Pvt. Ltd.')],                      
                        ]
    tbl=get_table(header_data_section,False)
    flow_obj.append(tbl)
    ##Certificate Text Section.
    certificate_data_section=[
                               [res.TXT_PTI_CERTIFICATE],                              
                             ]
    tbl=get_table(certificate_data_section,False)
    flow_obj.append(tbl)
    ##Main Data Section.
    ptiRepre=centralDataForPti(id,isAdv,receiptNumber)
    main_tbl_data=[
                    [para_txt('''<b>Sr#</b>'''),para_txt('''<b>PO #</b>'''),para_txt('''<b>PO Amount</b>'''),para_txt('''<b>Invoice #</b>'''),para_txt('''<b>Invoice Amount</b>'''),para_txt('''<b>Deduction</b>'''),para_txt('''<b>Net Amount</b>'''),para_txt('''<b>Receipt#</b>''')],
                    [para_txt(str(ptiRepre.serial_no)),para_txt(str(ptiRepre.po_number)),para_txt(ptiRepre.po_amount),para_txt(ptiRepre.inv_number),para_txt(ptiRepre.inv_amount),para_txt(ptiRepre.deduction),para_txt(ptiRepre.net_amt),para_txt(ptiRepre.receipt_no)],
                    [' ',' ',' ',' ',' ',' ',' ',' '],
                  ]
    tbl=get_table(main_tbl_data,True)
    flow_obj.append(tbl)
    ##deduction Reason.
    deduction_reason_data=[                           
                            [[para_txt('''<b><br/>Deduction Reason:</b>''')],[para_txt(ptiRepre.deduction_reason)]],                           
                          ]
    tbl=Table(deduction_reason_data,colWidths=[100,300])
    #tbl=get_table(deduction_reason_data,False)
    tbl_Style=TableStyle([
                         ('LINEBELOW',(0,1),(-1,-1),0.5,colors.black),
                        ])
    tbl.setStyle(tbl_Style)
    flow_obj.append(tbl)
    ## Central Section.

    tbl_middle_data=[
                      [],
                      [],
                      [[para_txt('''<font size=6>Authorized Representative(Signature)</font>''')]],
                      [[para_txt('''Name and Title:__________________''')]],
                      [[para_txt('''Date:__________________''')]],
                    ]
    tbl_middle=Table(tbl_middle_data)
    tbl_middle_style=TableStyle([
                                 ('LINEBELOW',(0,1),(-1,-4),0.5,colors.black),
                               ])
    tbl_middle.setStyle(tbl_middle_style)

    tbl_middle_datastamp=[
                          [logo_stamp_fishbowl(res.FISHBOWL_SIGN_PATH)],
                          [[para_txt('''<font size=6>Authorized Representative(Signature)</font>''')]],
                          [[para_txt('''Name and Title:__________________''')]],
                          [[para_txt('''Date:<u>'''+ datetime.date.today().strftime('%d-%m-%Y')+'''</u>''')]],
                         ]
    tbl_middle_stamp=Table(tbl_middle_datastamp)
    tbl_middle_style_stamp=TableStyle([
                                      ('LINEBELOW',(0,0),(-1,-4),0.5,colors.black),
                                     ])
    tbl_middle_stamp.setStyle(tbl_middle_style_stamp)
            


    tbl_stamp_data=[
                    [[para_txt('''<b>For and on Behalf of PMCL:</b>''')],[],[para_txt('''<b>For Contractor/Vendor</b>''')]],
                    [[tbl_middle],[tbl_middle],[tbl_middle_stamp]],
                   ]
    tbl_stamp_section=get_table(tbl_stamp_data,True)
    tbl_stamp_section_style=TableStyle([
                                        ('SPAN',(0,0),(-2,-2)),
                                        ('ALIGN',(0,0),(-1,-1),'CENTER')
                                       ])
    tbl_stamp_section.setStyle(tbl_stamp_section_style)

    flow_obj.append(tbl_stamp_section)
    
        
    ##Rules Section
    rules_data_section=[
                        [res.TXT_PTI_RULES],                              
                       ]
    tbl=get_table(rules_data_section,False)
    flow_obj.append(tbl)
    return flow_obj

def file_name_pti(id):
  inv=getInvoice(id)
  nm=str('attachment; filename='+'pti_'+inv.title+'.pdf')
  return nm

class ptiRepresentation:
    def __init__(self,serial_no,po_number,po_amount,inv_number,inv_amount,deduction,net_amt,receipt_no,deduction_reason):
        self.serial_no=serial_no
        self.po_number=po_number
        self.po_amount=po_amount
        self.inv_number=inv_number
        self.inv_amount=inv_amount
        self.deduction=deduction
        self.net_amt=net_amt
        self.receipt_no=receipt_no
        self.deduction_reason=deduction_reason

