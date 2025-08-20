from django.shortcuts import render,redirect
from KHSystemApp.models import AccountHead,PettyCashEntry
from .forms import AccountHeadForm,PettyCashEntryForm
from django.http import HttpResponse
import csv
from Estimate.views import *
from reportlab.platypus import Table,TableStyle,Paragraph,SimpleDocTemplate
from reportlab.lib.styles import (
    ParagraphStyle, 
    getSampleStyleSheet
)
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors



 #account Header URLS
def ah_index(request):
    ctx={'Headers':AccountHead.objects.all()}
    return render(request,'PettyCash/ah_index.html',ctx)
       
def ah_insert(request,id=0):   
    if request.method=="GET":
        if id==0:
           form=AccountHeadForm()
        else:
            obj_acchead=getAccountHead(id)
            form=AccountHeadForm(instance=obj_acchead)
        return render(request,"PettyCash/ah_insert.html",{'form':form})
        
    else: 
        if id==0:
            form=AccountHeadForm(request.POST)
        else: 
             obj_acchead=getAccountHead(id)
             form=AccountHeadForm(request.POST,instance=obj_acchead)
        if form.is_valid():
            form.save()
        return redirect('/pettycash/')


def ah_delete(request,id):
    acc_head=getAccountHead(id)
    acc_head.delete()
    return redirect('/pettycash/')

def getAccountHead(id):
    acc_head=AccountHead.objects.get(pk=id)
    return acc_head
################################
#Petty Cash  Section 
###############################
def getPettyCash(id):
    petty_cash=PettyCashEntry.objects.get(pk=id)
    return petty_cash


def pty_index(request):
    ctx={'pettycashEntries':output_pettycash()}
    return render(request,'PettyCash/pettycash_index.html',ctx)

def output_pettycash():
    pettyCashEntries=PettyCashEntry.objects.all()
    entries=[]
    remaining_balance=0
    rem_bal_display=crd=dbt=acc_head=''

    for en in pettyCashEntries:
        
        if en.credit==0.0:
            crd=' '
            remaining_balance=remaining_balance+en.debt
            acc_head=' '
        else:
            crd=en.credit


        if en.debt==0.0:
            dbt=' '
            remaining_balance=remaining_balance-en.credit
            acc_head=en.accountHead.accountHeadTitle
        else:
            dbt=en.debt
        
        if remaining_balance<0:
            rem_bal_display='('+str(round(-1*remaining_balance))+')'
        else:
            rem_bal_display=str(round(remaining_balance))

        ptyCshDisplay=pettyCashDisplay(en.id,en.pettyCashDate,en.narration,acc_head,en.branch,dbt,crd,rem_bal_display)
        entries.append(ptyCshDisplay)
   
    return entries

def petty_insert(request,id=0):
    if request.method=="GET":
        if id==0:
           form=PettyCashEntryForm()
        else:
            form=PettyCashEntryForm(instance=getPettyCash(id))
        return render(request,"PettyCash/pettycash_insert.html",{'form':form})      
    else: 
        if id==0:
            form=PettyCashEntryForm(request.POST)
        else:       
             form=PettyCashEntryForm(request.POST,instance=getPettyCash(id))
        if form.is_valid():
            form.save()
        return redirect('/pettycash/')
    

def petty_delete(request,id):
    pty_cash_entry=getPettyCash(id)
    pty_cash_entry.delete()
    return redirect('/pettycash/')


def petty_pdf(request,id):
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = pettycash_filename(id)
   pdf=SimpleDocTemplate(response)
   flow_obj=generate_pdf(id)
   pdf.build(flow_obj)
   return response

def pettycash_filename(id):
   petty_csh=PettyCashEntry.objects.get(pk=id)
   file_name=str('attachment; filename='+petty_csh.narration+'.pdf')
   return file_name

#Petty Cash Pdf Generation function.

def generate_pdf(id):
    flow_obj=[]
    petty_csh=PettyCashEntry.objects.get(pk=id)
    rs=''
    dr=cr=''
    if petty_csh.debt==0:
        rs=round(petty_csh.credit)
        cr=str(rs)
        dr=' '
    else:
        rs=round(petty_csh.debt)
        dr=str(rs)
        cr=' '
    
    left_side_data=[
                     ['PVC NO:',para('Islamabad')],
                     ['Date:',str(petty_csh.pettyCashDate)],
                     ['Rs:',str(rs)],
                    ]
    table_left=Table(left_side_data,colWidths=[70,100])
    tbl_style=TableStyle([
                          ('LINEBELOW',(1,0),(-1,-1),0.5,colors.black)
                         ])
    table_left.setStyle(tbl_style)

    #############################
    ## central section heading
    central_tbl_data=[
                     ['PAID TO:',[]],
                     ['RUPEES:',num2words(rs)],
                     ['A/C Head:',petty_csh.accountHead.accountHeadTitle],
                    ]
    table_center=Table(central_tbl_data,colWidths=[70,450],rowHeights=25)
    tbl_style_center=TableStyle([
                                 ('LINEBELOW',(1,0),(-1,-1),0.5,colors.black)
                                ])
    table_center.setStyle(tbl_style_center)
    #############################
    #Central Data Table.
    #############################

    petty_data=[
                ['','Details','Dr.','Cr.'],
                ['','','',''],
                ['',petty_csh.narration,dr,cr],
                ['','','',''],
                ['','Total',dr,cr],
               ]

    tbl_details=Table(petty_data,colWidths=[30,350,80,80])
    tbl_details_style=TableStyle([
                                  ('GRID',(0,0),(-1,-1),0.5,colors.black),
                                  ('ALIGN',(0,0),(-1,-1),'CENTER')
                                 ])
    tbl_details.setStyle(tbl_details_style)

    

    ################################
    #Footer Settings. Okeyed by, etc.
    ################################
    line='______________________'
    footer_data=[
                 [para_tag_br(line,'Okeyed by'),para_tag_br(line,'Approved by'),para_tag_br(line,'Received by')]
                ]
    tbl_footer=Table(footer_data,colWidths=[180,180,180])
    #################################

    
    header_data=[
                 [[logo_stamp_fishbowl(res.FISHBOWL_LOGO_PATH)],table_left],
                 [para('Petty Cash Voucher')],
                 [table_center],
                 [],
                 [tbl_details],
                 [],
                 [tbl_footer],
                 
                  [[logo_stamp_fishbowl(res.FISHBOWL_LOGO_PATH)],table_left],
                 [para('Petty Cash Voucher')],
                 [table_center],
                 [],
                 [tbl_details],
                 [],
                 [tbl_footer],
               ]
    
    tbl_head=Table(header_data,colWidths=[350,200])
    flow_obj.append(tbl_head)
    return flow_obj

def para(txt):
    txt_para=Paragraph('<u>'+txt+'</u>')
    return txt

def para_tag_br(txt,val): 
    txt=Paragraph(txt+'<br/>'+val)
    return txt


def petty_csv(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="petty_cash.csv"'  
    entries=output_pettycash()
    fieldsname=['Date','Narration','Account Head','Branch','Debt','Credit','Balance']
    #writer = csv.writer(response)
    writer=csv.DictWriter(response,fieldnames=fieldsname)
    writer.writeheader()  
    for ent in entries:  
        #writer.writerow([ent.dt,ent.narration,ent.account_head,ent.branch,ent.debt,ent.credit,ent.balance])  
        writer.writerow({'Date':ent.dt,'Narration':ent.narration,'Account Head':ent.account_head,'Branch':ent.branch,'Debt':ent.debt,'Credit':ent.credit,'Balance':ent.balance})  
    return response  
       

class pettyCashDisplay:
    def __init__(self,id__,dt,narration,account_head,branch,debt,credit,balance):
        self.id__=id__
        self.dt=dt
        self.narration=narration
        self.account_head=account_head
        self.branch=branch
        self.debt=debt
        self.credit=credit
        self.balance=balance


