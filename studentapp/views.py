from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def add(request):
    a=request.GET['n1']
    b=request.GET['n2']
    c=int(a)+int(b)
    return render(request,'answer.html',{'c':c})
