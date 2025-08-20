from reportlab.platypus import Paragraph
class res:
    FISHBOWL_LOGO_PATH='static\css\images\_fishbowl_logo.PNG'
    FISHBOWL_SIGN_PATH='static\css\images\company_pti_stamp.PNG'
    FISHBOWL_STAMP_PATH='static\css\images\_fishbowl_stamp.png'
    JAZZ_LOGO_PATH='static\css\images\jazz_logo.PNG'

    TXT_PTI_CERTIFICATE=Paragraph('''<para align=left><font size=8><b><u>Certificate of Permission to Invoice</u></b><br/>This is to certify that goods/services required and described under the above agreement/purchase order have been<br/>'''
                                 +'''completed to the extent of invoice amounts mentioned below. The vendor is permitted to submit below mentioned<br/>'''
                                 +'''invoice/invoices with PMCL Finance department;</font></para>'''
                                 )
    
    TXT_PTI_RULES=Paragraph('''<para align=left><font size=8><u><b>Note:</b></u><br/>1) This Certificate is merely a permission to raise invoice and does not entitle the holder of any outstanding claims<br/>'''
                            +'''with respect to the Services rendered until and unless the invoice is approved as per PMCL Authority Matrix<br/>'''
                            +'''2) Amounts mentioned are exclusive of taxes<br/>'''
                            +'''3) Receipts # to be filled by respective PMCL user department</font></para>'''       
                           ) 
                         

    
    TXT_ESTIMATE_SPECIFIC=Paragraph('''<para align=left><font size=6>1. Please do not withheld income tax, Fish Bowl will deduct on behalf of PMCL''' 
                          +'''<br/>2. All payments should be made by cheques crossed A/C Payee Only with title Fishbowl Pvt Ltd.''' 
                          +'''    Bank A/c Title: FISH BOWL (PVT) LTD. Standard Chartered Bank, Account # 01732138201''' 
                          +'''    Branch Name: Z-Block Branch, Lahore. Branch Code: 0137 ---IBAN: PK36 SCBL 0000 0017 3213 8201''' 
                          +'''<br/>    Our NTN is 4126367-7  Our PNTN is 4126367-7</font></para>''')
                                    

    TXT_REIMBURSEMENT_SPECIFIC=Paragraph('''<para><font size=6>1. Please do not withheld income tax, Fish Bowl will deduct on behalf of PMCL'''
                                   +'''<br/>2. All payments should be made by cheques crossed A/C Payee Only with title Fishbowl Pvt Ltd.'''
                                   +'''<br/>3. Please verify the bill within ten days from the date of delivery'''
                                   +'''      If we do not hear from you within this period we will consider the bill as correct'''
                                   +'''      Bank A/c Title: FISH BOWL (PVT) LTD. Standard Chartered Bank, Account # 01732138201'''
                                   +'''      Branch Name: Z-Block Branch, Lahore. Branch Code: 0137 ---IBAN: PK36 SCBL 0000 0017 3213 8201'''
                                   +'''<br/>Our NTN is 4126367-7  Our PNTN is 4126367-7</font></para>'''
                                   )

    HEAD_OFFICE=Paragraph('''<para><font size=7><strong><u>Head Office:</u></strong>181/1,1st Floor, Y Block(Commercial) Phase 3,DHA ,Lahore Tel:- +92 42 35692464</font></para>''')
    REGIONAL_OFFICE_ISL=Paragraph('''<para><font size=6.5><strong><u>Regional Office:</u></strong> 2 A, Al Fateh Market ,Street 3, G-9/3,1st Floor, Y Block(Commercial) Islamabad Tel:- +92 51 8734008-9</font></para> ''')
    REGIONAL_OFFICE_KHR=Paragraph('''<para><font size=7><strong><u>Regional Office:</u></strong>C-28 B, Street 24,Commercial Area<br/>Phase 2(Ext),DHA.,Karachi</font></para>''')

    ESTIMATE_ADDRESS=Paragraph('''<font size=7>To,<br/><b>M/S. Pakistan Mobile Communication Ltd(Jazz) </b><br/>Address: 1-A, IBC Building, F-8 Markaz,Islamabad,<br/>Pakistan,NTN#0802694-7</font>''')

    REIMBURSEMENT_ADDRESS=Paragraph('''<font size=7>To,<br/><b>M/S. Pakistan Mobile Communication Ltd(Jazz) </b><br/>Address: 1-A, IBC Building, F-8 Markaz,<br/>Islamabad,Pakistan<br/>NTN#0802694-7<br/>Contact Person:<br/><b>Brand:Jazz</b></font>''')
    