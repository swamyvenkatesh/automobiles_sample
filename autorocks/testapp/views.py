# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Insertdata
import xml.etree.ElementTree as ET

# Create your views here.
def index(request):
    """  Home Page """
    text = "Welcome to Autorox"
    dic = dataDict(request)
    alldata=dic.values()
    add=[]
    for each in alldata:
        add.extend(each)
    roomdataata=dic["rooms"]
    halldata=dic["Halls"]   
    return render(request, 'home.html', {'data':add,'info':roomdataata,'process':halldata})

def dataDict(request):
    """ Data Dictionary """
    dataStruct = {
        "rooms":["bedroom","kitchenroom","poojaroom"],
        "Halls":["drawinghall","livinghall"]
        }
    return dataStruct

def getdatafmexcel(request):
    if request.method=="GET":        
        val_from_ajax = request.GET.get("getinfo")
        details=Insertdata.objects.filter(name=val_from_ajax)
        data1 = {}
        for i in details:            
            data1['name']=i.name.capitalize()           
            values_list = i.values.split(",")
            values_list.pop()
            data1['values']=values_list
        return JsonResponse(data1)
    
def donedata(request):
    """ Data Update functionality """
    if request.method=="GET":        
        senddata1=request.GET.get('datainfo')
        splitinfo=senddata1.split("close")              
        newdat=",".join(splitinfo)        
        dialoginfo=request.GET.get('dialoginfo')        
        Insertdata.objects.filter(name=dialoginfo).update(values=newdat)        
        senddata={"name":"success"}
        return JsonResponse(senddata)
    
def seachdetails(request):
    """ Search functionality """
    if request.method=="GET":
        searchdetails=request.GET.get('searchinfo')
        dict1 = dataDict(request)
        result = []
        add=[]
        message=""
        for each in dict1.values():
            add.extend(each)        
        for i in add:
            if i.__contains__(searchdetails):
                result.append(i.capitalize())
            else:
                message="Result not found"            
        
        main_root = ET.Element('ul')        
        for i in result:
            li_tab = ET.SubElement(main_root, 'li')
            a_tab = ET.SubElement(li_tab, "a", href="#", id="{0}".format(i), onclick="myfunc()").text=str(i)               

        results_data = ET.tostring(main_root).replace('clas','class')

        search_result = {"r_list":results_data,"popupinfo":message}
        return JsonResponse(search_result)  