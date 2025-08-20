from django.db import models
import datetime
import django


class AccountHead(models.Model):
    accountHeadEntranceDate=models.DateField(default=django.utils.timezone.now)
    accountHeadTitle=models.CharField(max_length=200)
    class Meta:
        db_table='AccountHead'
    def __str__(self):
        return self.accountHeadTitle

class PettyCashEntry(models.Model):
    pettyCashDate=models.DateField(default=django.utils.timezone.now)
    narration=models.CharField(max_length=250)
    branch=models.CharField(max_length=20,default='ISB')
    debt=models.FloatField(default=0.0)
    credit=models.FloatField(default=0.0)
    accountHead=models.ForeignKey(AccountHead,on_delete=models.CASCADE,related_name='accountHeads',null=False)
    class Meta:
        db_table='PettyCashEntry'
    def __str__(self):
        return self.narration

# Create your models here.
class ClientServices(models.Model):
    name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=14)
    email=models.EmailField(max_length=254,default='@gmail.com')
    address=models.CharField(max_length=200,default='ISL')
    #invoices=models.CharField(max_length=100,default='invoice000')
    
    #pic  #gendre  #DateHired #DOB  #address

    class Meta:
        db_table='ClientServices'
    
    def __str__(self):
        return self.name


class Clients(models.Model):
     name=models.CharField(max_length=100)
     phonenumber=models.CharField(max_length=14)
     email=models.EmailField(max_length=254,default='@mobilink.com')
     company=models.CharField(max_length=50,default='Jazz/Mobilink')
     class Meta:
        db_table='Clients'
     def __str__(self):
        return self.name


################################################### 
#premium
#class Company(models.Model):
     #name=models.CharField(max_length=100)
     #db_table='Company'
#def __str__(self):
        #return self.name
####################################################



class TaxAuthority(models.Model):
    BOOL_CHOICES=(
                   (True,'YES'),
                   (False,'No')
                 )
    taxauthority=models.CharField(max_length=200,default='PST/SST')
    taxrate=models.FloatField(default=0.0)
    isReimbursed=models.BooleanField(default=False,choices=BOOL_CHOICES)
    class Meta:
       db_table='TaxAuthority'
    def __str__(self):
       return self.taxauthority


class Vendor(models.Model):
    name=models.CharField(max_length=200,default='ccc')
    ntn=models.IntegerField(default=0)
    address=models.CharField(max_length=254,default='LHR')
    logo=models.ImageField(upload_to='images/')
    class Meta:
        db_table='Vendors'
    def __str__(self):
        return self.name

class Invoices(models.Model):
    title=models.CharField(max_length=500,default=" ")
    fishbowlid=models.CharField(max_length=20)
    vendorInvoiceId=models.CharField(max_length=20)
    #change it to estimateReceivedDate
    submissionToClientDate=models.DateField(default=django.utils.timezone.now)
    vendors=models.ForeignKey(Vendor,on_delete=models.SET_NULL,related_name='vendors',null=True)
    clientservices=models.ForeignKey(ClientServices,on_delete=models.SET_NULL,related_name='clientservices',null=True)
    taxauthority=models.ForeignKey(TaxAuthority,on_delete=models.SET_NULL,related_name='taxauthories',null=True)
    client=models.ForeignKey(Clients,on_delete=models.SET_NULL,related_name='clients',null=True)
    advancepayment=models.FloatField(default=30.0)
    discountOffered=models.FloatField(default=0)
    notes=models.TextField(blank=True,default='Nil')

    class Meta:
        db_table='Invoices'
    def __str__(self):
        return self.title


#Stage 1 Of Operation. Quotation

class Quotation(models.Model):    
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    quotationReceivedDate=models.DateField(default=django.utils.timezone.now)
    quotationFile=models.FileField(upload_to='documents/')
    notes=models.TextField(blank=True,default='Nil')
    class Meta:
        db_table="Quotation"
    def __str__(self):
        txt=str('Received Date:'+str(self.quotationReceivedDate)+'<br/>Notes:-<br/>'+self.notes)



class EstimateType(models.Model):
    BOOL_CHOICES=(
                   (True,'YES'),
                   (False,'No')
                 )
    EstimateTypeTitle=models.CharField(max_length=300)
    isTaxable=models.BooleanField(default=True,choices=BOOL_CHOICES)
    class Meta:
        db_table="EstimateType"
    def __str__(self):
       return self.EstimateTypeTitle


#Stage 2 Of Operation. Estimate
class Estimate(models.Model):
    Format_Choices=(
                     ('LN','Line Numbering'),
                     ('HN','Header Numbering'),
                   )
    estimateType=models.ForeignKey(EstimateType,on_delete=models.CASCADE,related_name='estTypes',null=True)
    estimateGenerationDate=models.DateField(default=django.utils.timezone.now)
    sharedToClientDate=models.DateField(default=django.utils.timezone.now)
    reference=models.CharField(max_length=250,default="Email")
    description=models.TextField()
    quantity=models.TextField(blank=True)
    rate=models.TextField(blank=True)
    amount=models.TextField()
    notes=models.CharField(blank=True,default='Nil',max_length=300)
    estimateFormat=models.CharField(max_length=25,choices=Format_Choices,null=False)
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    estimate_bytes_pdf=models.BinaryField(blank=True)
    class Meta:
        db_table="Estimate"

# Stage 3 Of Operation . Purchase Requsition No.
class PurchaseRequsition(models.Model):    
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    prRequestedDate=models.DateField(default=django.utils.timezone.now)
    prReceivedDate=models.DateField(default=django.utils.timezone.now,blank=True)
    prNumber=models.CharField(max_length=20,blank=True)
    notes=models.TextField(blank=True,default='Nil')
    
    class Meta:
        db_table="PurchaseRequsition"

# Stage 4 Of Operation . Purchase Order(PO).
class PurchaseOrder(models.Model):    
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    poRequestedDate=models.DateField(default=django.utils.timezone.now)
    poReceivedDate=models.DateField(default=django.utils.timezone.now,blank=True)
    poNumber=models.CharField(max_length=20,blank=True)
    notes=models.TextField(blank=True,default='Nil')
    poFile=models.FileField(upload_to='documents/',blank=True)
    
    class Meta:
        db_table="PurchaseOrder"

# Stage 5 Of Operation . Reimbursement Invoice(RI).
class Reimbursement(models.Model):    
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    reInvNumber=models.CharField(max_length=20,blank=True)
    notes=models.TextField(blank=True,default='Nil')
    reInvDate=models.DateField(default=django.utils.timezone.now,blank=True)
    class Meta:
        db_table="Reimbursement"

class Pti(models.Model):
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    ptiDate=models.DateField(default=django.utils.timezone.now,blank=True)
    deduction=models.CharField(default='Nil',max_length=20)
    notes=models.TextField(blank=True,default='Nil')
    class Meta:
        db_table="PermissionToInvoice"


class JazzReceiptNoRequest(models.Model):
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    receiptReqDate=models.DateField(default=django.utils.timezone.now,blank=True)
    notes=models.TextField(blank=True,default='Nil')
    initialPtiFile=models.FileField(upload_to='documents/',blank=True)
    advRiFile=models.FileField(upload_to='documents/',blank=True)
    class Meta:
        db_table="JazzReceiptNumberRequest"

class ReceiptNumberReceived(models.Model):
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    receiptReceivedDate=models.DateField(default=django.utils.timezone.now,blank=True)
    receiptNumber=models.CharField(max_length=20)
    notes=models.TextField(blank=True,default='Nil')
    class Meta:
        db_table="ReceiptNumber"


class SalesTaxInvoice(models.Model):
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    salesTaxInvoiceRequestedDate=models.DateField(default=django.utils.timezone.now,blank=True)
    salesTaxInvoiceReceivedDate=models.DateField(default=django.utils.timezone.now,blank=True)
    salesTaxFile=models.FileField(upload_to='documents/',blank=True)
    notes=models.TextField(blank=True,default='Nil')
    class Meta:
        db_table="SalesTaxInvoice"

class AssembleExportEmail(models.Model):
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    emailText=models.TextField()
    emailsPdfFile=models.FileField(upload_to='documents/',blank=False)
    class Meta:
        db_table="AssembleEmailText"


class iPortalPreparation(models.Model):
    invoice=models.OneToOneField(Invoices,on_delete=models.CASCADE,null=False,primary_key=True)
    uploadedDate=models.DateField(default=django.utils.timezone.now,blank=True)
    ptiPdfFile=models.FileField(upload_to='documents/',blank=True)
    riPdfFile=models.FileField(upload_to='documents/',blank=True)
    notes=models.TextField(blank=True,default='Nil')
    class Meta:
        db_table="iPortalPreparation"




        




        


    



   



