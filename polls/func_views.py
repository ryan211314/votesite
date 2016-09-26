from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse,HttpResponseNotFound
from .models import *
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission,User
from .forms import UploadFileForm
import os
from django.views.generic.edit import FormView


class FileFieldView(FormView):
    form_class = UploadFileForm
    template_name = 'polls/upload.html'
    success_url = '/polls/'
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def handle_uploaded_file(f):
    print os.path.abspath('.')+'\\uploadfile'
    with open(os.path.abspath('.')+'\\uploadfile','wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            instance = Doc(upload = request.FILES['file'],is_activated=True)
            instance.save()
            #handle_uploaded_file(request.FILES['file'])
            return HttpResponse('success')
    else:
        form = UploadFileForm()
    #return FileFieldView().as_view()
    return render(request,'polls/upload.html',{'form':form})





def change_password(request):
    template_response = views.password_change(request)
    # Do something with `template_response`
    return template_response


def alogin(request):
    errors= []
    account=None
    password=None
    if request.method == 'POST' :
        if not request.POST.get('account'):
            errors.append('Please Enter account')
        else:
            account = request.POST.get('account')
        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password= request.POST.get('password')
        if account is not None and password is not None :
             user = authenticate(username=account,password=password)
             if user is not None:
                 if user.is_active:
                     login(request,user)
                     return HttpResponseRedirect('/polls/')
                 else:
                     errors.append('disabled account')
             else :
                  errors.append('invaild user')
    
    return render(request, 'account/login.html', {'errors': errors})
def register(request):
    errors= []
    account=None
    password=None
    password2=None
    email=None
    CompareFlag=False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('Please Enter account')
        else:
            account = request.POST.get('account')
        if not request.POST.get('password'):
            errors.append('Please Enter password')
        else:
            password= request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('Please Enter password2')
        else:
            password2= request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append('Please Enter email')
        else:
            email= request.POST.get('email')

        if password is not None and password2 is not None:
            if password == password2:
                CompareFlag = True
            else :
                errors.append('password2 is diff password ')


        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag :
            user=User.objects.create_user(account,email,password)
            user.is_active=True
            user.save
            res = '<a href="/polls/"">return</a>'
            return HttpResponse(res)
            #return HttpResponseRedirect('/polls/')


    
    return render(request, 'account/register.html', {'errors': errors})

def alogout(request):
    logout(request)
    return HttpResponseRedirect('/polls/')



                        
