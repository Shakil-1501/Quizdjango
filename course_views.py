# Core Django imports.
from django.views.generic import ListView
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg, Max, Min, Sum
from django.conf import settings 
from django.core.mail import send_mail
from django.core.paginator import Paginator
# Blog application imports.
from lms.models.course_model import Course
from lms.models.course_model import Question,Responses
from lms.models.student_model import Profile
from lms.models.course_model import Quiz



class CourseListView(ListView):
    model = Course
    context_object_name = "courses"
    template_name = "lms/course/home.html"


def course(request): 
    #model = Course
    #context_object_name = "questions"
    #template_name = "lms/course/quiz.html"
    #question = Question()
    courses = Course.objects.all()
    context = {'courses': courses}


    return render(request,'lms/course/course.html',context)

def fetch_questions(request):
    questions = Question.objects.all()
    quizs = Quiz.objects.first()
    context = dict()
    context.update({'questions':questions})
    
    context.update({'quizs':quizs})
    '''
    subject = 'welcome to GFG world'
    message = 'Hi Jagat, A question is added'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = ['jagatabhay@gmail.com'] 
    send_mail( subject, message, email_from, recipient_list ) 
    '''
    

    return render(request,'lms/course/quiz3.html',context)


    

def fetch_questions_oneatatime(request):
    obj = Question.objects.all()

    count = Question.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)
    
    return render(request,'lms/course/quiz.html',{'obj':obj,'questions':questions,'count':count})    


def display_lp(request):
    quizs = Quiz.objects.first()
    context = {'quizs':quizs}
    return render(request,'lms/quiz2.html',context)

def Edit_quiz(request):
    return render(request,'admin/')  

def preview_quiz(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'lms/course/quizs.html',context)

def quiz_lp(request):
    quizs=Quiz.objects.all()
    context = {'quizs':quizs}
    return render(request,'lms/course/quizlp.html',context)




def compute_stats(request):
    profiles= Profile.objects.all()
    context= dict()
    context.update({'profiles':profiles})
    context.update(Profile.objects.all().aggregate(Avg('marks')))
    context.update(Profile.objects.all().aggregate(Min('marks')))
    context.update(Profile.objects.all().aggregate(Max('marks')))
    context.update(Profile.objects.all().aggregate(Avg('Time_taken')))
    
    return render(request,'lms/course/course.html',context)


def enter_comment(request):
    responses = Responses.objects.all()
    context = {'responses':responses}
    if request.method == "POST":
       
       comments = request.POST.get['comments']
       responses = Responses(comments=comments)
       responses.save()
       return render(request,'lms/course/responses.html')
    else:
        return render(request,'lms/course/responses.html',context)   


def take_quiz(request,id):
     context = {'id': id}

     return render(request,'quiz.html',context)  
