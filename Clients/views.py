from django.shortcuts import render,redirect
from KHSystemApp.models import *
from .forms import ClientsForm

def index(request):
    context={'clients':Clients.objects.all() }
    return render(request,"Clients/index.html",context)

    



def delete_(request,id):
    client=Clients.objects.get(pk=id)
    client.delete()
    return redirect('/clients/')


def details_(request,id):
    clnt=Clients.objects.get(pk=id)
    ctx={'clients':clnt}
    return render(request,'Clients/details.html',ctx)

def insert_(request,id=0):
    if request.method=="GET":
        if id==0:
            form=ClientsForm()
        else:
            clt=Clients.objects.get(pk=id)
            form=ClientsForm(instance=clt)
        return render(request,'Clients/insert.html',{'form':form})
    
    else:
        if id==0:
            form=ClientsForm(request.POST)
        else:
            obj_clnt=Clients.objects.get(pk=id)
            form=ClientsForm(request.POST,instance=obj_clnt)
    if form.is_valid():
        form.save()
    return redirect('/clients/')



        



    
    











