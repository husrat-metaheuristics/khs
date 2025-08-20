
      $(document).ready(function (){


        //////////////////////////////////////////
        
        $('#add_row').click(function(){
          
          var markup="<tr>"
                      +"<td><input type='checkbox' name='record'></td>"
                      +"<td>"
                      +"<textarea class='detail-header' name='dtl-header' placeholder='----Type Heading ------' rows='1' cols='78'></textarea>"
                      +"<hr>"
                      +"<textarea name='details' class='details-txt-area' cols='78' rows='5'></textarea>"
                      +"</td>"
                      +"<td>"
                      +"<textarea class='qty-header' name='qty-header'  rows='1' cols='2'></textarea>"
                      +"<hr>"
                      +"<textarea name='quantity' class='qty-txt-area' cols='2' rows='5'></textarea>"
                      +"</td>"
                      +"<td>"
                      +"<textarea class='rate-header' name='rt-header' rows='1' placeholder='Header Value' cols='11'></textarea>"
                      +"<hr>"
                      +"<textarea name='rate' class='rate-txt-area' cols='11' rows='5'></textarea>"
                      +"</td>"
                      +"<td>"
                      +"<textarea class='amount-header' name='amt-header'  rows='1' placeholder='Header Value' cols='11'></textarea>"
                      +"<hr>"
                      +"<textarea name='amount' class='amount-txt-area' cols='11' rows='5'></textarea></td>"
                      +"</tr>";
                      $("table tbody").append(markup);
                      
        });
        
        $('#delete_row').click(function(){
          
          $('table tbody').find('input[name="record"]').each(function(){

                 if($(this).is(":checked")){

                  $(this).parents("tr").remove();
                 }
          });
                      
        }); 

        $('#preview').click(function(){
          detail_txt_full='';
          qty_txt_full='';
          rate_txt_full='';
          amount_txt_full='';

          //validate and load logic into textarea
          $('table tbody').find('tr').each(function(){
            var qty='';
            var rate='';
            var amount='';
            var detail='';
            var qty_header='';
            var rate_header='';
            var amount_header='';
            var detail_header='';

                 $(this).find('td').each(function(){
                     $(this).find('textarea').each(function(){

                      nme=$(this).attr('name');
                      txt_value=$(this).val();
          
                      if(nme=='details')
                      {
                        detail=txt_value;
                      }
                      else if(nme=='dtl-header')
                      {
                        detail_header=txt_value;
                      }
                       else if(nme=='quantity')
                      {
                        qty=txt_value;
                      
                      }
                      else if(nme=='qty-header')
                      {
                        qty_header=txt_value;
                      }
                        else if(nme=='rate')
                      {
                         rate=txt_value;
                      }
                      else if(nme=='rt-header')
                      {
                         rate_header=txt_value;
                      }

                       else if(nme=='amount')
                      {
                         amount=txt_value;
                      }
                      else if(nme=='amt-header')
                      {
                        amount_header=txt_value; 
                      }
          
                      
                     });//each textarea search

                 });//each column search

                     detail=detail.split('\n');
                     qty=qty.split('\n');
                     rate=rate.split('\n');
                     amount=amount.split('\n');
                     //alert('details='+detail.length+'qty='+qty.length+'rate='+rate.length+'amount='+amount.length);
                    
                     if((detail.length>=qty.length)&&(detail.length>=rate.length)&&(detail.length>=amount.length))
                     {
                       
                        qty_txt_full+='<H>'+qty_header+'</H>'+'\n';
                        rate_txt_full+='<H>'+rate_header+'</H>'+'\n';
                        amount_txt_full+='<H>'+amount_header+'</H>'+'\n';
                        detail_txt_full+='<H>'+detail_header+'</H>'+'\n';

                     for(i=0 ;i<detail.length;i++)
                      {

                        detail_txt_full+='<L>'+detail[i]+'</L>'+'\n';
                        if(i<qty.length)
                        {
                          qty_txt_full+='<L>'+qty[i]+'</L>'+'\n';
                        }
                        else{
                           qty_txt_full+='<L>'+''+'</L>'+'\n';
                        }

                        if(i<rate.length)
                        {
                          rate_txt_full+='<L>'+rate[i]+'</L>'+'\n';
                        }
                        else{
                          rate_txt_full+='<L>'+''+'</L>'+'\n';
                        }
                        if(i<amount.length)
                        {
                          amount_txt_full+='<L>'+amount[i]+'</L>'+'\n';
                        }
                        else{
                          amount_txt_full+='<L>'+''+'</L>'+'\n';
                        }
                       
                      }
                    }
                    else{
                      //logic for displaying error message inside the div.
                    }

                    detail_txt_full+='[endblock]'+'\n';
                    qty_txt_full+='[endblock]'+'\n';
                    rate_txt_full+='[endblock]'+'\n';
                    amount_txt_full+='[endblock]'+'\n';

                    $('#txt-details').val(detail_txt_full);
                    $('#txt-qty').val(qty_txt_full);
                    $('#txt-rate').val(rate_txt_full);
                    $('#txt-amount').val(amount_txt_full);

             });//end of row

            
        });

        //Fill the table with text for editing.
        if($('#txt-details').val()||$('#txt-qty').val()||$('#txt-rate').val()||$('#txt-amount').val())
        {
            details=$('#txt-details').val().split('[endblock]');
            qty=$('#txt-qty').val().split('[endblock]');
            rate=$('#txt-rate').val().split('[endblock]');
            amount=$('#txt-amount').val().split('[endblock]');
            //clear the data from the form.description,form.qty,form.rate,form.amount
             
            
            $('#txt-details').val('');
            $('#txt-qty').val('');
            $('#txt-rate').val('');
            $('#txt-amount').val('');

            //load the data into table.
            $('table tbody').find('textarea').each(function(){
               nm=$(this).attr('name');
               $(this).parents("tr").remove();
            });

               for(i=0;i<(details.length-1);i++)
               {
                
                dt_txt=break_by_line(details[i]);
                qt_txt=break_by_line(qty[i]);
                rt_txt=break_by_line(rate[i]);
                mt_txt=break_by_line(amount[i]);

                var dt_hdr='';
                var qt_hdr='';
                var rt_hdr='';
                var mt_hdr='';
               //alert('\n------------\n'+dt_txt+'\n----------------\n'+qt_txt+'\n------------\n'+rt_txt+'\n------------\n'+mt_txt);
        
                internal_dt=internal_qt=internal_rt=internal_mt='';

                for(idx=0;idx<(dt_txt.length-1);idx++)
                {
                 
        

                  if(dt_txt[idx].search("<H>")!=-1)
                  {

                    dt_hdr="<textarea class='detail-header' name='dtl-header' placeholder='----Type Heading ------' rows='1' cols='78'>"+removeTags('<H>','</H>',dt_txt[idx])+"</textarea>"+"<hr>";
                    qt_hdr="<textarea class='qty-header' name='qty-header'  rows='1' cols='2'>"+removeTags('<H>','</H>',qt_txt[idx])+"</textarea>"+"<hr>";
                    rt_hdr= "<textarea class='rate-header' name='rt-header' rows='1' placeholder='Header Value' cols='11'>"+removeTags('<H>','</H>',rt_txt[idx])+"</textarea>"+"<hr>";
                    mt_hdr="<textarea class='amount-header' name='amt-header'  rows='1' placeholder='Header Value' cols='11'>"+removeTags('<H>','</H>',mt_txt[idx])+"</textarea>"+"<hr>";

                   // alert(dt_hdr+"\n-------\n"+qt_hdr+"\n-------\n"+rt_hdr+"\n-------\n"+mt_hdr)
                  }
                  else{
                    internal_dt+=removeTags('<L>','</L>',dt_txt[idx])+'\n';
                    internal_qt+=removeTags('<L>','</L>',qt_txt[idx])+'\n';
                    internal_rt+=removeTags('<L>','</L>',rt_txt[idx])+'\n';
                    internal_mt+=removeTags('<L>','</L>',mt_txt[idx])+'\n';
                  }



                }

                var markup="<tr>"
                      +"<td><input type='checkbox' name='record'></td>"
                      +"<td>"+dt_hdr+"<textarea name='details' class='details-txt-area' cols='78' rows='5'>"+internal_dt+"</textarea>"+"</td>"
                      +"<td>"+qt_hdr+"<textarea name='quantity' class='qty-txt-area' cols='2' rows='5'>"+internal_qt+"</textarea>"+"</td>"
                      +"<td>"+rt_hdr+"<textarea name='rate' class='rate-txt-area' cols='11' rows='5'>"+internal_rt+"</textarea>"+"</td>"
                      +"<td>"+mt_hdr+"<textarea name='amount' class='amount-txt-area' cols='11' rows='5'>"+internal_mt+"</textarea>"+"</td>"
                      +"</tr>";
                      $("table tbody").append(markup);

               }

            


             function break_by_line(txt)
             {
               return(txt.split('\n'));
             }

             function removeTags(start_tag,end_tag,txt)
             {
                   txt=txt.replace(start_tag,'');
                   return(txt.replace(end_tag,''));
             }

          }

          
          
           
        
      });
 