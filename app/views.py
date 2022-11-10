from tkinter import E
from winreg import REG_WHOLE_HIVE_VOLATILE
from django import http
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import json
def home(request):

    return render(request,'home.html')
def search(request):
    devicename = request.GET["device"]
    if(devicename =='pc'):
        return render(request,'pc.html', context={'output' : computernadscreen.objects.all()})
    else:
        return render(request,'printer.html',context={'output' : printer.objects.all()})

def search1(request):
    searchcat= request.GET["searchcat"]
    searchfield = request.GET["searchfield"]
    mydictionary={}
    if(searchfield  or  searchcat ):
        allpc = ''
        if searchcat == "Bldg" : allpc = computernadscreen.objects.filter(Bldg=searchfield).all()
        if searchcat == "Floor" : allpc = computernadscreen.objects.filter(Floor=searchfield).all()
        if searchcat == "Department" : allpc = computernadscreen.objects.filter(Department=searchfield).all()
        if searchcat == "room" : allpc = computernadscreen.objects.filter(room=searchfield).all()
        if searchcat == "Socket" : allpc = computernadscreen.objects.filter(Socket=searchfield).all()
        if searchcat == "Barcode" : allpc = computernadscreen.objects.filter(Barcode=searchfield).all()
        if searchcat == "PC_SN" : allpc = computernadscreen.objects.filter(PC_SN=searchfield).all()
        if searchcat == "PC_Name" : allpc = computernadscreen.objects.filter(PC_Name=searchfield).all()
        if searchcat == "pc_Make" : allpc = computernadscreen.objects.filter(pc_Make=searchfield).all()
        if searchcat == "pc_Model" : allpc = computernadscreen.objects.filter(pc_Model=searchfield).all()
        if searchcat == "pc_CPU" : allpc = computernadscreen.objects.filter(pc_CPU=searchfield).all()
        if searchcat == "pc_RAM" : allpc = computernadscreen.objects.filter(pc_RAM=searchfield).all()
        if searchcat == "pc_Username" : allpc = computernadscreen.objects.filter(pc_Username=searchfield).all()
        if searchcat == "pc_Warranty" : allpc = computernadscreen.objects.filter(pc_Warranty=searchfield).all()
        if searchcat == "pc_PO" : allpc = computernadscreen.objects.filter(pc_PO=searchfield).all()
        if searchcat == "screen_Make" : allpc = computernadscreen.objects.filter(screen_Make=searchfield).all()
        if searchcat == "scrren_size" : allpc = computernadscreen.objects.filter(scrren_size=searchfield).all()
        if searchcat == "screen_SN" : allpc = computernadscreen.objects.filter(screen_SN=searchfield).all()
        if searchcat == "screen_Barcode" : allpc = computernadscreen.objects.filter(screen_Barcode=searchfield).all()
        if searchcat == "screen_PO" : allpc = computernadscreen.objects.filter(screen_PO=searchfield).all()
        if searchcat == "screen_Model" : allpc = computernadscreen.objects.filter(screen_Model=searchfield).all()
        mydictionary = {  'output' : allpc}
    else: mydictionary = {  'output' : computernadscreen.objects.all()}
    return render(request,'pc.html',context = mydictionary)

def search2(request):
    searchcat= request.GET["searchcat"]
    searchfield = request.GET["searchfield"]
    if(searchfield  or  searchcat ):
        allprinter='' 
        if searchcat == "Bldg" : allprinter = printer.objects.filter(Bldg=searchfield).all()
        if searchcat == "Floor" : allprinter = printer.objects.filter(Floor=searchfield).all()
        if searchcat == "room" : allprinter = printer.objects.filter(room=searchfield).all()
        if searchcat == "Socket" : allprinter = printer.objects.filter(Socket=searchfield).all()
        if searchcat == "Barcode" : allprinter = printer.objects.filter(Barcode=searchfield).all()
        if searchcat == "Make" : allprinter = printer.objects.filter(make=searchfield).all()
        if searchcat == "Model" : allprinter = printer.objects.filter(Model=searchfield).all()
        if searchcat == "SN" : allprinter = printer.objects.filter(SN=searchfield).all()
        if searchcat == "Warranty" : allprinter = printer.objects.filter(Warranty=searchfield).all()
        if searchcat == "address" : allprinter = printer.objects.filter(address=searchfield).all()
        if searchcat == "PO" : allprinter = printer.objects.filter(PO=searchfield).all()
        mydictionary = {'output' :allprinter}
    else:
        mydictionary = {  'output' : printer.objects.all()}
    return render(request,'printer.html',context = mydictionary)
def addpc(request):
    return render(request,'addpc.html')
def addprinter(request):
    return render(request,'addprinter.html')
def upload(request):
    obj = computernadscreen()
    obj.Barcode = request.GET["Barcode"]
    obj.Bldg = request.GET["Bldg"]
    obj.Floor = request.GET["Floor"]
    obj.Department = request.GET["Department"]
    obj.Socket = request.GET["Socket"]
    obj.room = request.GET["room"]
    obj.PC_SN = request.GET["PC_SN"]
    obj.PC_Name = request.GET["PC_Name"]
    obj.pc_Make = request.GET["pc_Make"]
    obj.pc_Model = request.GET["pc_Model"]
    obj.pc_CPU = request.GET["pc_CPU"]
    obj.pc_RAM = request.GET["pc_RAM"]
    obj.pc_Username = request.GET["pc_Username"]
    obj.pc_Warranty = request.GET["pc_Warranty"]
    obj.pc_PO = request.GET["pc_PO"]
    obj.screen_Barcode = request.GET["screen_Barcode"]
    obj.screen_SN = request.GET["screen_SN"]
    obj.screen_Make = request.GET["screen_Make"]
    obj.screen_Model = request.GET["screen_Model"]
    obj.screen_PO = request.GET["screen_PO"]
    obj.scrren_size = request.GET["scrren_size"]
    obj.save()
    mydic =  {'output':computernadscreen.objects.all()}
    return render(request,'pc.html',context=mydic)

def upload2(request):
    obj = printer()
    obj.Barcode = request.GET["Barcode"]
    obj.Bldg = request.GET["Bldg"]
    obj.Floor = request.GET["Floor"]
    obj.Department = request.GET["Department"]
    obj.Socket = request.GET["Socket"]
    obj.room = request.GET["room"]
    obj.SN = request.GET["SN"]
    obj.Make = request.GET["Make"]
    obj.Model = request.GET["Model"]
    obj.Warranty = request.GET["Warranty"]
    obj.PO = request.GET["PO"]
    obj.address = request.GET["address"]
    obj.save()
    mydic =  {'output':printer.objects.all()}
    return render(request,'printer.html',context=mydic)

def delete(request):
    id= request.GET["id"]
    device= request.GET["device"]
    if(device == 'pc'):
        computernadscreen.objects.filter(id=id).delete()
        mydic =  {'output':computernadscreen.objects.all()}
        return render(request,'pc.html',context=mydic)
    else:
        printer.objects.filter(id=id).delete()
        mydic =  {'output':printer.objects.all()}
        return render(request,'printer.html',context=mydic)

def edit(request):
    id= request.GET["id"]
    device= request.GET["device"]
    if(device == 'pc'):
        mydic =  {'output':computernadscreen.objects.filter(id=id).all()}
        return render(request,'pcedit.html',context=mydic) 
    else:
        mydic =  {'output':printer.objects.filter(id=id).all()}
        return render(request,'printeredit.html',context=mydic)      
def save(request):
    id= request.GET["id"]
    obj = computernadscreen.objects.get(id__exact=id)
    obj.Barcode = request.GET["Barcode"]
    obj.Bldg = request.GET["Bldg"]
    obj.Floor = request.GET["Floor"]
    obj.Department = request.GET["Department"]
    obj.Socket = request.GET["Socket"]
    obj.room = request.GET["room"]
    obj.PC_SN = request.GET["PC_SN"]
    obj.PC_Name = request.GET["PC_Name"]
    obj.pc_Make = request.GET["pc_Make"]
    obj.pc_Model = request.GET["pc_Model"]
    obj.pc_CPU = request.GET["pc_CPU"]
    obj.pc_RAM = request.GET["pc_RAM"]
    obj.pc_Username = request.GET["pc_Username"]
    obj.pc_Warranty = request.GET["pc_Warranty"]
    obj.pc_PO = request.GET["pc_PO"]
    obj.screen_Barcode = request.GET["screen_Barcode"]
    obj.screen_SN = request.GET["screen_SN"]
    obj.screen_Make = request.GET["screen_Make"]
    obj.screen_Model = request.GET["screen_Model"]
    obj.screen_PO = request.GET["screen_PO"]
    obj.scrren_size = request.GET["scrren_size"]
    obj.save()
    mydic =  {'output':computernadscreen.objects.filter(id=id).all()}
    return render(request,'pc.html',context=mydic)


def save1(request):
    id= request.GET["id"]
    obj = printer.objects.get(id__exact=id)
    obj.Barcode = request.GET["Barcode"]
    obj.Bldg = request.GET["Bldg"]
    obj.Floor = request.GET["Floor"]
    obj.Department = request.GET["Department"]
    obj.Socket = request.GET["Socket"]
    obj.room = request.GET["room"]
    obj.SN = request.GET["SN"]
    obj.Make = request.GET["Make"]
    obj.Model = request.GET["Model"]
    obj.address = request.GET["address"]
    obj.Warranty = request.GET["Warranty"]
    obj.PO = request.GET["PO"]
    obj.save()
    mydic =  {'output':printer.objects.filter(id=id).all()}
    return render(request,'printer.html',context=mydic)



def view(request):
    id= request.GET["id"]
    device= request.GET["device"]
    if(device == 'pc'):
       mydic =  {'output':computernadscreen.objects.filter(id=id).all()}
       return render(request,'pcview.html',context=mydic) 
    else:
        mydic =  {'output':printer.objects.filter(id=id).all()}
        return render(request,'printerview.html',context=mydic)           