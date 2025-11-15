from django.contrib import admin
from .models import Student
from .models import subject
from .models import Enrollment

 
admin.site.register(Student)
admin.site.register(subject)
admin.site.register(Enrollment)



# Register your models here.
