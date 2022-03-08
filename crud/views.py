from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from crud.models import Registration
from .forms import Reg_form
# Create your views here.
def home(request):
      context={}
      return render(request,'crud/home.html',context)

def display(request):
      obj=Registration.objects.all()
      context={'obj':obj}
      return render(request,'crud/home.html',context)

def edit(request,user_id):
      obj=Registration.objects.get(pk=user_id)
      form=Reg_form(instance=obj)
      context={'form':form,'obj':obj}
      if request.method=='POST':
            form=Reg_form(request.POST,instance=obj)
            if form.is_valid():
                  form.save(commit=True)
                  return render(request,'crud/display.html',context)
      else:
            
            return render(request,'crud/edit.html',context)
      return render(request,'crud/edit.html',context)
def delete_record(request,user_id):
      obj=Registration.objects.get(pk=user_id)
      obj.delete()
      return render(request,'crud/home.html')
def login_page(request):
      return render(request,'crud/login.html')
def login_user(request):
      if request.method=='POST':
            username=request.POST['username']
            email=request.POST['email']
            # user=Registration(username=username,email=email)
            user=authenticate(username=username,email=email)
            if user:
                  
                     login(request,user)
                  # return render(request,'crud/home.html',{'success':'You successfully loged in','username':username})
                     return HttpResponse('You successfully loged in ')
            else:
                  return HttpResponse('Login failed')
                  # return render(request,'crud/login.html',{'failure':'login failed'})
      return render(request,'crud/login.html')

            
      