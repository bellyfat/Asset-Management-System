from django.shortcuts import render
from django.http import *
from django.template import loader
from .models import *
# from .forms import PostForm

# Create your views here.

def log(request):
    check=sessiontable.objects.filter(id=1)[0]
    if check.status=="active":
        s="Already Logged in as "+check.username+" Go to <a href='/loginwork/log/home'>home</a>"        
        return HttpResponse(s)
    elif request.method == "POST":
        employeeid=request.POST['employeeid']
        password=request.POST['pass']
        b=userstable.objects.filter(employeeid=employeeid,password=password)
        if b.count()!=0:
            sessiontable.objects.filter(id=1).update(username=employeeid,status="active")
            return HttpResponseRedirect('/loginwork/log/home')
        else:
            return HttpResponse("try again")    
    else:    
        return render(request,'login.html')

def home(request):
    check=sessiontable.objects.filter(id=1)[0]
    if check.status=="inactive":
        s="Session has expired go to <a href='/loginwork/log'>login</a>"        
        return HttpResponse(s)
    elif request.GET.get('mybtn'):
        sessiontable.objects.filter(id=1).update(username="none",status="inactive")
        return HttpResponseRedirect('/loginwork/log')
    else:
        a0=userstable.objects.filter(role="admin")[0].employeeid
        return render(request,'home.html',{"a" : (check.username==a0)})

def assets(request):
    check=sessiontable.objects.filter(id=1)[0]
    if check.status=="inactive":
        s="Session has expired go to <a href='/loginwork/log'>login</a>"        
        return HttpResponse(s)
    elif request.GET.get('mybtn'):
        sessiontable.objects.filter(id=1).update(username="none",status="inactive")
        return HttpResponseRedirect('/loginwork/log')            
    else:
        a = assetstable.objects.all()
        for i in a:
            if request.GET.get("mybtn"+str(i.id)):
               b = elementstable.objects.filter(assetid=str(i.id))        
               template2 = loader.get_template('assetmgmt.html')
               context2 = {
               'b':b,
               }
               return HttpResponse(template2.render(context2,request))
            if request.GET.get("adelbtn"+str(i.id)):
               assetstable.objects.filter(id=str(i.id)).delete()
               return HttpResponseRedirect('/loginwork/log/assets')
            if request.GET.get("aeditbtn"+str(i.id)):
               a1=request.GET['modelno'+i.modelno]
               a2=request.GET['make'+i.make]
               a3=request.GET['productno'+i.productno]
               a4=request.GET['purchaseno'+i.purchaseno] 
               assetstable.objects.filter(id=str(i.id)).update(modelno=a1,make=a2,productno=a3,purchaseno=a4)
               return HttpResponseRedirect('/loginwork/log/assets')    
        template = loader.get_template('assets.html')
        context = {
        'a':a,
        }
        return HttpResponse(template.render(context,request))
    
        
def purchases(request):
    check=sessiontable.objects.filter(id=1)[0]
    if check.status=="inactive":
        s="Session has expired go to <a href='/loginwork/log'>login</a>"        
        return HttpResponse(s)        
    elif request.GET.get('mybtn'):
        sessiontable.objects.filter(id=1).update(username="none",status="inactive")
        return HttpResponseRedirect('/loginwork/log')    
    else:
        a = purchasestable.objects.all()
        for i in a:
            if request.GET.get("btn"+str(i.purchaseno)):
               b = assetstable.objects.filter(purchaseno=i.purchaseno)        
               template2 = loader.get_template('assets.html')
               context2 = {
               'a':b,
               }
               return HttpResponse(template2.render(context2,request))
            if request.GET.get("pdelbtn"+str(i.purchaseno)):
               purchasestable.objects.filter(purchaseno=i.purchaseno).delete()   
               return HttpResponseRedirect('/loginwork/log/purchases')
            if request.GET.get("peditbtn"+str(i.purchaseno)):
               a1=request.GET['serialno'+i.purchaseno]
               a2=request.GET['warrantystartdate'+i.purchaseno]
               a3=request.GET['warrantyenddate'+i.purchaseno]
               purchasestable.objects.filter(purchaseno=str(i.purchaseno)).update(serialno=a1,warrantystartdate=a2,warrantyenddate=a3)
               return HttpResponseRedirect('/loginwork/log/purchases')     

        a1 = assetstable.objects.all()
        for i in a1:
            if request.GET.get("mybtn"+str(i.id)):
               b1 = elementstable.objects.filter(assetid=str(i.id))        
               template3 = loader.get_template('assetmgmt.html')
               context3 = {
               'b':b1,
               }
               return HttpResponse(template3.render(context3,request)) 
            if request.GET.get("adelbtn"+str(i.id)):
               assetstable.objects.filter(id=str(i.id)).delete()  
            if request.GET.get("aeditbtn"+str(i.id)):
               a1=request.GET['modelno'+i.modelno]
               a2=request.GET['make'+i.make]
               a3=request.GET['productno'+i.productno]
               a4=request.GET['purchaseno'+i.purchaseno] 
               assetstable.objects.filter(id=str(i.id)).update(modelno=a1,make=a2,productno=a3,purchaseno=a4)
               return HttpResponseRedirect('/loginwork/log/purchases')    

        template = loader.get_template('purchases.html')
        context = {
        'a':a,
        }
        return HttpResponse(template.render(context,request))

def adduser(request):
    check=sessiontable.objects.filter(id=1)[0]
    a0=userstable.objects.filter(role="admin")[0].employeeid        
    if check.status=="inactive":
        s="Session has expired go to <a href='/loginwork/log'>login</a>"        
        return HttpResponse(s)
    elif check.username!=a0:
        s="Not authorized to visit this page... go to <a href='/loginwork/log/home'>home</a>"        
        return HttpResponse(s)    
    elif request.GET.get('mybtn'):
        sessiontable.objects.filter(id=1).update(username="none",status="inactive")
        return HttpResponseRedirect('/loginwork/log')
    elif request.method == "POST":
        name = request.POST['name']
        employeeid = request.POST['employeeid']
        email = request.POST['email']
        password = request.POST['pass']
        b=userstable.objects.filter(employeeid=employeeid)
        c=userstable.objects.filter(email=email)
        if b.count()==0 and c.count()==0:
            a=userstable()
            a.name = name
            a.employeeid = employeeid
            a.email = email
            a.password = password
            a.ROLE = "user"
            a.save()
            return HttpResponseRedirect('/loginwork/log/home')
        else:
            return HttpResponse("use different credentials... go back to <a href='/loginwork/log'>login</a>")
    else:
        return render(request,'adduser.html')



def addasset(request):    
    check=sessiontable.objects.filter(id=1)[0]
    if check.status=="inactive":
        s="Session has expired go to <a href='/loginwork/log'>login</a>"        
        return HttpResponse(s)  
    elif request.GET.get('mybtn'):
        sessiontable.objects.filter(id=1).update(username="none",status="inactive")
        return HttpResponseRedirect('/loginwork/log')      
    elif request.method == "POST":        
        b=assetstable()
        b.modelno = request.POST['modelno']
        b.make = request.POST['make']
        b.productno =  request.POST['productno']
        b.purchaseno = "none"
        b.save()
        a=['HDD','MBD','SAS CARD','DVD RW DRIVE','GRAPHICS CARD','KEYBOARD','MOUSE','SMPS','MEMORY','CPU FAN','SYSTEM FAN','PROCESSOR','FRONT PANEL SWITCH','MONITOR']
        for i in range(14):
            c=elementstable()        
            c.elementtype = a[i] 
            c.assetid = b.id
            c.slno = request.POST['serialno'+str(i+1)]
            c.ctno = request.POST['ctno'+str(i+1)]
            c.spno = request.POST['spno'+str(i+1)]
            c.save()
        return HttpResponseRedirect('/loginwork/log/home')  
    else:
        return render(request,'addasset.html')

def addpurchase(request):
    check=sessiontable.objects.filter(id=1)[0]
    if check.status=="inactive":
        s="Session has expired go to <a href='/loginwork/log'>login</a>"        
        return HttpResponse(s)  
    elif request.GET.get('mybtn'):
        sessiontable.objects.filter(id=1).update(username="none",status="inactive")
        return HttpResponseRedirect('/loginwork/log')      
    elif request.method == "POST":        
        b=purchasestable()
        b.purchaseno = request.POST['purchaseno']
        b.serialno = request.POST['serialno']
        b.warrantystartdate =  request.POST['startdate']
        b.warrantyenddate = request.POST['enddate']
        b.save()
        a = int(request.POST['assets'])
        for i in range(a): 
            ano = request.POST['asset'+str(i)]
            assetstable.objects.filter(id=ano).update(purchaseno = b.purchaseno)
        return HttpResponseRedirect('/loginwork/log/home')  
    else:
        return render(request,'addpurchase.html')

