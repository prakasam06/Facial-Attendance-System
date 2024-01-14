from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40,null=True,blank=True,unique=True)
    def __str__(self):
        return f"{self.name}"


class Class_obj(models.Model):
    name = models.CharField(max_length=10,null=True,blank=True)
    batch = models.CharField(max_length=10,null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students_department')
    def __str__(self):
        return f"{self.name}--> {self.batch}"
    
    

class Profile(models.Model):
    roll_number = models.CharField(max_length=10,null=True,blank=True)
    overall_attendance = models.CharField(max_length=10,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_profile_obj')
    is_OD = models.BooleanField(default=False)
    is_ML = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=50,null=True,blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_of',null=True,blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department_key',null=True,blank=True)
    class_obj = models.ForeignKey(Class_obj, on_delete=models.CASCADE, related_name='students_class_obj',null=True,blank=True)
    batch = models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
        return f"{self.user.first_name}"
    
class Subject(models.Model):
    name = models.CharField(max_length=40,null=True,blank=True)
    class_obj = models.ForeignKey(Class_obj, on_delete=models.CASCADE, related_name='class_key_object',null=True,blank=True)
    handled_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subject_is_handled_by',null=True,blank=True)
    def __str__(self):
        return f"{self.name}---> {self.class_obj__batch}"

