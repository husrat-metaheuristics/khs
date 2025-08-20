import itertools
from reportlab.platypus import Paragraph
class EstimateDisplay:
  def __init__(self,description,qty,taxrate,rate,amount,serial_no,isHeader):
    self.description=description
    self.qty=qty
    self.taxrate=taxrate
    self.rate=rate
    self.amount=amount
    self.serial_no=serial_no
    self.isHeader=isHeader

def para_tag_taxrate(txt):
  txt_para=Paragraph('''<para align=center><font size=6>'''+txt+'''</font></para>''')
  return txt_para

def split_by_tag(item,tag_):
    return item.split(tag_)

def strip_spaces(itm):
    return itm.strip()

def remove_tags(itm,beginTag,endTag):
    if itm.find('\r')!=-1:
        itm=itm.replace('\r','') 
    itm=itm.replace(beginTag,'')
    return itm.replace(endTag,'')


def prepare_estimate_display(description,quantity,rate,amount,estimateFormat,taxauth,isForPreview):
    
    display_list=[]
    block_spliter='[endblock]'
    des_list=split_by_tag(description,block_spliter)
    qty_list=split_by_tag(quantity,block_spliter)
    rate_list=split_by_tag(rate,block_spliter)
    amount_list=split_by_tag(amount,block_spliter)

    s_idx=1  #serial No for display
    for (des_itm,qty_itm,rt_itm,amt_itm) in itertools.zip_longest(des_list,qty_list,rate_list,amount_list):
        des_block=split_by_tag(strip_spaces(des_itm),'\n')
        qty_block=split_by_tag(strip_spaces(qty_itm),'\n')
        rt_block=split_by_tag(strip_spaces(rt_itm),'\n')
        amt_block=split_by_tag(strip_spaces(amt_itm),'\n')

        serial_no=des_txt=qty_txt=rt_txt=amt_txt=''
        isHeader=True
        
        for (des_line,qty_line,rt_line,amt_line) in itertools.zip_longest(des_block,qty_block,rt_block,amt_block):
            
            startTag=''
            endTag=''
            tax_Rate=''
            if des_line.find('<H>')!=-1 and qty_line.find('<H>')!=-1 and rt_line.find('<H>')!=-1 and amt_line.find('<H>')!=-1:
                startTag='<H>'
                endTag='</H>'
                tax_Rate=''
                isHeader=True
                if estimateFormat=='LN':
                    serial_no=''
                else:
                    serial_no=s_idx
                    if remove_tags(des_line,'<H>','</H>')!='':
                     s_idx=s_idx+1
            else:
                startTag='<L>'
                endTag='</L>'
                isHeader=False
                if isForPreview:
                    tax_Rate=taxrate_col_txt(taxauth,'\n')
                else:
                    tax_Rate=para_tag_taxrate(taxrate_col_txt(taxauth,'<br/>'))
                if estimateFormat=='HN':
                    serial_no=''
                else:
                    serial_no=s_idx
                    if remove_tags(des_line,'<L>','</L>')!='':
                      s_idx=s_idx+1
                
            des_txt=remove_tags(des_line,startTag,endTag)
            qty_txt=remove_tags(qty_line,startTag,endTag)
            rt_txt=remove_tags(rt_line,startTag,endTag)
            amt_txt=remove_tags(amt_line,startTag,endTag)
            #############################
            if rt_txt.isdigit() or amt_txt.isdigit():
               dig=float("{:.2f}".format(float(rt_txt)))
               rt_txt=f'{dig:,}'
               rt_txt=str(rt_txt+'0')
               
            if amt_txt.isdigit():
               di=float("{:.2f}".format(float(amt_txt)))
               amt_txt=f'{di:,}'
               amt_txt=str(amt_txt+'0')
            

            if des_txt!='':
              estimate_obj=EstimateDisplay(des_txt,qty_txt,tax_Rate,rt_txt,amt_txt,serial_no,isHeader)
              display_list.append(estimate_obj)
                 
    return display_list

def taxrate_col_txt(taxauth,txt__):
    ttl=' '
    if taxauth.isReimbursed:
        ttl='Reimbursable'
    else:
        ttl='Non Reimbursable'
    txt=str(taxauth.taxauthority+'('+str(taxauth.taxrate)+'%)'+txt__+'('+ttl+')')
    return txt


def amount_calculation(amt):
    amount_list=split_by_tag(amt,'[endblock]')
    amount_total=0.0
    for itm in amount_list:
        amt_block=split_by_tag(strip_spaces(itm),'\n')
        startTag=''
        endTag=''
        for inner_itm in amt_block:
            if inner_itm.find('<H>')!=-1:
                startTag='<H>'
                endTag='</H>'
            else:
                startTag='<L>'
                endTag='</L>'
            txt=remove_tags(inner_itm,startTag,endTag)
            if txt.isdigit():
                amount_total+=float(txt)
    return amount_total

def createLink(url__,name__):
    return str('<a target="_blank" href='+'"../media/'+str(url__)+'"'+'>'+name__+'</a>')
    

def createButton(template_url,id__,name__):
   strPortion1=str('<a href=\"{%'+' '+'url'+' '+template_url+' ')
   strPortion2="{}".format(id__)
   strPortion3=str(' %}\" class=\"btn btn-outline-success\">'+name__+'</a>')
   finalStr="{}{}{}".format(strPortion1,int(strPortion2),strPortion3)
   return finalStr 
   #str('<a href="{% url'+' '+template_url+' '+id__+ ' %}" class="btn btn-outline-success">'+name__+'</a>')

    








        

        
        

