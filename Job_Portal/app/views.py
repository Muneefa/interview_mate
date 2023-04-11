from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from .forms import QuestionForm
from .forms import FeedbackForm

# from django.views.generic import View
# from django.urls import reverse_lazy
from .models import Job,result,Notification, Feedback
from .models import Question
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    jobs = Job.objects.all()
    user_id = request.user.id
    username = request.user.username
    feedback = Feedback.objects.filter(user_id=user_id)
    print('feedback is',feedback)
    print(user_id,username)
    design_and_creative = []
    information_technology = []
    design_and_development = []
    sales_and_marketing=[]
    mobile_and_Application=[]
    construction=[]
    for job in jobs:
        if job.choose_field == 'Design & creative':
            design_and_creative.append(job)
        elif job.choose_field == 'Information technology':
            information_technology.append(job)
        elif job.choose_field == 'Design & development':
            design_and_development.append(job)
        elif job.choose_field == 'sales & marketing':
            sales_and_marketing.append(job)
        elif job.choose_field == 'mobile Application':
            mobile_and_Application.append(job) 
        elif job.choose_field == 'construction':
            construction.append(job)   
        elif job.choose_field == 'contentWriter':
            construction.append(job)    
    return render (request,'home.html',{'user_id':user_id,'username':username,'feedback':feedback,'design_and_creative': design_and_creative, 'information_technology': information_technology, 'design_and_development': design_and_development,'sales_and_marketing':sales_and_marketing,' mobile_and_Application': mobile_and_Application,'construction':construction})

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'register.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        print("user is",user)
              
        if user is not None and not user.is_superuser:
            login(request,user)
            if username == 'dimpal' and pass1 == 'dimpal@123':
                  return redirect('recruiter') 
            elif username == 'Recruiter' and pass1 == 'recruiter@123':
                  return redirect('add_question')     
            else:
                  return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def jobdetalis(request,job_id,user_id):
    job = get_object_or_404(Job, pk=job_id)
    user= get_object_or_404(User, pk=user_id)
    print("user is",user)
    print("job is",job.job_title)
    user = request.user
    
    users=User.objects.get(id=user.id)
    # user_id=users.id
    print("we got",users.id)
    if request.method == 'POST':
       if 'form1_submit' in request.POST: # Check if Form 1 was submitted
            if not request.session.get('form1_submitted'):
                    name = request.POST.get('name')
                    email = request.POST.get('email')
                    
                    # Get the list of question IDs from the form
                    question_ids = request.POST.getlist('question_id')
                    # Loop through the questions and calculate the score
                    score = 0
                    for question_id in question_ids:
                        # Get the user's answer for this question
                        answer_key = 'answer_' + question_id
                        user_answer = request.POST.get(answer_key)
                        print(user_answer)
                        
                        # Get the correct answer for this question from the database
                        question = Question.objects.get(pk=question_id)
                        correct_answer = question.answer
                        
                        # Check if the user's answer matches the correct answer
                        if user_answer == correct_answer:
                            score += 1
                    # Save the user's score and other data to the database
                    quiz_result = result(name=name,user_id=users, email=email, score=score,field=job.choose_field,job_title=job.job_title,company_name =job.company_name )
                    quiz_result.save()
                    request.session['form1_submitted'] = True
                    messages.success(request, 'your answer was successfully submitted.')
            else:
                messages.warning(request, 'You have already wrote the test.')        

       elif 'form2_submit' in request.POST: 
            if not request.session.get('form2_submitted'):
                name = request.POST.get('name')
                email = request.POST.get('email') 
                notification=Notification(name=name,user_id=users,email=email,field=job.choose_field,job_title=job.job_title,company_name =job.company_name )
                notification.save()
                request.session['form2_submitted'] = True
                messages.success(request, 'your Request was successfully submitted.')
            else:
                messages.warning(request, 'You have already Notified the Recriter.') 
                   
    if job.choose_field=='Information technology':
        question = Question.objects.filter(choose_field='Information technology')
    elif job.choose_field == 'Design & development':
        question = Question.objects.filter(choose_field='Design & development')
    elif job.choose_field == 'sales & marketing':
        question = Question.objects.filter(choose_field='sales & marketing')
    elif job.choose_field == 'mobile Application':
        question = Question.objects.filter(choose_field='mobile Application')
    elif job.choose_field == 'construction':
        question = Question.objects.filter(choose_field='construction')
    elif job.choose_field == 'contentWriter':
        question = Question.objects.filter(choose_field='contentWriter')
    if job.choose_field == 'Design & creative':
        question = Question.objects.filter(choose_field='Design & creative')
    return render(request, 'jobdetails.html', {'job': job,'question':question})

    
# class QuizView(View):
    template_name = 'quiz.html'

    def get(self, request):
        question = Question.objects.order_by('?').first()
        context = {
            'question': question,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        question_id = request.POST.get('question_id')
        selected_answer = request.POST.get('answer')

        question = Question.objects.get(pk=question_id)
        score = 0
        if selected_answer == question.answer_1:
            score = 1
        elif selected_answer == question.answer_2:
            score = 2
        elif selected_answer == question.answer_3:
            score = 3

        quiz_result = QuizResult.objects.create(name=name, email=email, score=score)

        return redirect(reverse_lazy('quiz_result', args=[quiz_result.pk]))    


def details(request):
    results = result.objects.all()
    notification=Notification.objects.all()
    return render(request,'Recruiter/details.html', {'results': results,'notification':notification})

@login_required(login_url='login')
def recriterPage(request):
    return render (request,'Recruiter/index.html')
def postjob(request):
    form_submitted = False
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data
            job = Job()
            job.job_title = form.cleaned_data['job_title']
            job.company_name = form.cleaned_data['company_name']
            job.salary = form.cleaned_data['salary']
            job.logo_upload = form.cleaned_data['logo_upload']
            job.location = form.cleaned_data['location']
            job.description = form.cleaned_data['description']
            job.choose_field = form.cleaned_data['choose_field']
            job.save()
            form_submitted = True
            # Create a new instance of the JobForm with empty data dictionary
            form = JobForm()
            
            
    else:
        form = JobForm()
    
    # 
    context = {'form': form, 'form_submitted': form_submitted}
    return render(request,'Recruiter/postjob.html',context)

def send_feedback(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form_submitted = False 
    if request.method == 'POST':
        
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback=Feedback()
            feedback.feedback = form.cleaned_data['feedback']
            feedback.user=user
            feedback.save()
            form_submitted = True
            form=FeedbackForm()
            # Feedback.objects.create(user=user, feedback=feedback)
            # return HttpResponseRedirect('/')
    else:
        form = FeedbackForm()

    context = {
        'form': form,
        'user': user,
        'form_submitted': form_submitted
    }
    return render(request, 'Recruiter/feedback.html', context)

@login_required(login_url='login')
def add_question(request):
    form_submitted = False
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # questionForm=QuestionForm()
            # questionForm.question_text = form.cleaned_data['question_text']
            # questionForm.answer_1= form.cleaned_data['answer_1']
            # questionForm.answer_2= form.cleaned_data['answer_2']
            # questionForm.answer_3= form.cleaned_data['answer_3']
            # questionForm.answer= form.cleaned_data['answer']
            # questionForm.choose_field=form.cleaned_data['choose_field']
            form.save()
            form_submitted = True
            form = QuestionForm()
            # return redirect('question_list')  # Redirect to list of all questions
    else:
        form = QuestionForm()
    context={'form':form,'form_submitted': form_submitted}    
    return render(request, 'Recruiter/question.html',context)

def LogoutPage(request):
    logout(request)
    return redirect('login')