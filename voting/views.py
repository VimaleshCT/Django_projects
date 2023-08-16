
import array
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
globalcnt =dict()
arr = ['Java','Python','c++','c','Javascript','PHP','SQL','MYSQL','HTML','CSS','DotNET']
def index(request):
  

   
   mydict = {
   "arr" : arr 
   }
   return render(request,'index.html',context=mydict)


def getquery(request):
    q =request.GET['languages']
    if q in globalcnt:
        globalcnt[q] = globalcnt[q]+1
    else:
        #1st occurence
        globalcnt[q]=1
    mydict ={
        "arr" : arr,
        "globalcnt" : globalcnt
        
    }
    return render(request,"index.html",context=mydict)


def sortdata(request):
   global globalcnt
   globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))    
   mydict = {
   "arr" : arr, 
   "globalcnt" : globalcnt

   }
   return render(request,'index.html',context=mydict)