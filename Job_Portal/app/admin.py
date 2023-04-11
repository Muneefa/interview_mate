from django.contrib import admin
from .models import Job
from .models import Question,result,Notification,Feedback

admin.site.register(Job)
admin.site.register(Question)
admin.site.register(Notification)
admin.site.register(result)
admin.site.register(Feedback)

# admin.site.register(FormStatus)

