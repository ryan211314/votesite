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
from .func_views import *




def cmsIndex(request):

    username = request.META.get('USERNAME',None)
    password = '123qweASD'
    user = authenticate(username=username,password=password)
    if user is not None:
        pass
    else:
        User.objects.create_user(username=username, email="test@mail.com", password=password)

    users = User.objects.all().count()
    



    context = { 'user':username , 'users':users }
    return render(request,'cms/businesshall.html',context)

def cmsWeb(request,filename):
    return render(request,'cms/'+filename+'.html')

@login_required(login_url="/polls/account/login/")
def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_gradequestion_list = GradeQuestion.objects.order_by('-pub_date')[:5]
    doc_list = Doc.objects.all()
    user = request.user
    request.session['favor'] = 'blue'

    context = {'latest_question_list': latest_question_list,
               'latest_gradequestion_list':latest_gradequestion_list,
               'doc_list':doc_list, 
               'user':user}
    
    
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    print request.session.keys()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET","POST"])
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

def readDoc(request,doc_id):
    doc = Doc.objects.get(pk=doc_id)
    with open(doc.upload.path,'r') as f:
        #print f.read()
        return HttpResponse(f.read())

import os.path
import xlwt
def answerQuestion(request,question_id):
    question = Question.objects.get(pk=question_id)
    question_text = question.question_text
    choice_list = question.choice_set.all()
    doclist = Doc.objects.all()
    for doc in doclist:
        print os.path.splitext(doc.upload.path)[1]
        if 'docx' in os.path.splitext(doc.upload.path)[1] :
            import docx

            def readDocx(docName):
                fullText = []
                doc = docx.Document(docName)
                paras = doc.paragraphs
                for p in paras:
                    fullText.append(p.text)
                return '\n'.join(fullText)

            def judgeAnswer(docContent,question_text,choice_list):
                
                for choice in choice_list:
                    if choice.choice_text in docContent and question_text in docContent:
                        return choice.choice_text 
                
                return 'not found'


            return HttpResponse(judgeAnswer(readDocx(doc.upload.path),question_text,choice_list))



def not_found_view(reuqest):
    pass

                        
