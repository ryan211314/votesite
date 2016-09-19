from django.shortcuts import get_object_or_404, render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question,GradeQuestion
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission,User


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


@login_required(login_url="/polls/account/login/")
def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_gradequestion_list = GradeQuestion.objects.order_by('-pub_date')[:5]
    user = request.user
    context = {'latest_question_list': latest_question_list,'latest_gradequestion_list': latest_gradequestion_list,'user':user}
    
    
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if request.user in question.person.all():

            return HttpResponse('you have voted')
        else:
            selected_choice.votes += 1
            question.person.add(request.user)
            selected_choice.person.add(request.user)
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))