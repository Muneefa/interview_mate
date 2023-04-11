"""Job_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('jobdetalis/<int:job_id>/<int:user_id>',views.jobdetalis,name='jobdetalis'),
    path('recruiter/',views.recriterPage,name='recruiter'),
    path('postjob/',views.postjob,name='postjob'),
    path('add_question/',views.add_question,name='add_question'),
    path('details/',views.details,name='details'),
    path('send_feedback/<int:user_id>',views.send_feedback,name='send_feedback'),



    # path('QuizView/',views.QuizView,name='QuizView'),







]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
