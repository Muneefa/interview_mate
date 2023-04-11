from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    logo_upload = models.ImageField(upload_to='logos/')
    location = models.CharField(max_length=100)
    description = models.TextField()
    choose_field = models.CharField(max_length=200, choices=[('Design & creative', 'Design & creative'), ('Design & development', 'Design & development'), ('sales & marketing', 'sales & marketing'
    ),('mobile Application','mobile Application'),('construction','construction'),('Information technology','Information technology')])

    def __str__(self):
        return self.job_title
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
    choose_field = models.CharField(max_length=200,default='default_value', choices=[('Design & creative', 'Design & creative'), ('Design & development', 'Design & development'), ('sales & marketing', 'sales & marketing'
    ),('mobile Application','mobile Application'),('construction','construction'),('Information technology','Information technology')])


    def __str__(self):
        return self.question_text   

class result(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    score = models.IntegerField() 
    field=  models.CharField(max_length=200)   
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100) 

class Notification(models.Model):  
    name = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    field=  models.CharField(max_length=200) 
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100) 


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s feedback"