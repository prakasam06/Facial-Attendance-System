from django.core.management.base import BaseCommand 
from django.contrib.auth.models import Group,User
from base_app.models import *
from base_app.db_objects import user_groups,departments,classes,mentors,subjects,students



class Command(BaseCommand): 
    help = 'Creates Groups at initial level'
    def handle(self, *args, **kwargs):
        for group in user_groups:
            Group.objects.get_or_create(name=group)
            print(f"{group} is created")
            email = f"{group}@gmail.com"
            user = User.objects.create(username=group,password=group,email=email,first_name=f"{group}_first",last_name=f"{group}_last")
            user_group = Group.objects.get(name=group)
            user.groups.add(user_group)
            user.save()
            Profile.objects.create(user=User.objects.get(username=group))
        for department in departments:
            Department.objects.get_or_create(name=department['name'])
            print(f"{department['name']} is created")
        for class_key in classes:
            Class_obj.objects.get_or_create(name=class_key['name'],batch=class_key['batch'],department=Department.objects.get(name=class_key['department']))
            print(f"{class_key['name']} is created")

        for mentor in mentors:
            user = User.objects.create(username=mentor['username'],password=mentor['email'],
                                            email=mentor['email'],first_name=mentor['username'],last_name=mentor['username'])
            mentor_group = Group.objects.get(name="MENTOR")
            user.groups.add(mentor_group)
            user.save()
            Profile.objects.create(user=user,is_mentor=True,roll_number=mentor['roll'],password=mentor['email'])
            print(f"{mentor['username']} is created")
        
        for subject in subjects:
            Subject.objects.create(name=subject['name'],
                                          class_obj=Class_obj.objects.get(name=subject['class']),
                                          handled_by=User.objects.get(email=subject['handled_by']))
            print(f"{subject['name']} is created")
        for student in students:
            user = User.objects.create(username=student['username'],password=student['email'],
                                            email=student['email'],first_name=student['username'],last_name=student['username'])
            student_group = Group.objects.get(name="STUDENT")
            user.groups.add(student_group)
            user.save()
            Profile.objects.create(user=user,roll_number=student['roll'],batch=student['batch'],
                                   department=Department.objects.get(name=student['department']),
                                   class_obj=Class_obj.objects.get(name=student['class']),
                                   mentor=User.objects.get(email=student['mentor']),password=mentor['email'])
            print(f"{student['username']} is created")

    