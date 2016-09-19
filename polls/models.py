from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import Permission,User
# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    person = models.ManyToManyField(User)
    def __str__(self):        
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class GradeQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    person = models.ManyToManyField(User)
    def __str__(self):        
        return self.question_text

class Grade(models.Model):
    question = models.ForeignKey(GradeQuestion, on_delete=models.CASCADE)
    grade = models.IntegerField(default=0)
    person = models.ManyToManyField(User,default=None)
    def __str__(self):
        return str(self.grade)

# class Person(models.Model):
#     #first_name = models.CharField(max_length=30)
#     #last_name = models.CharField(max_length=30)
#     IDENTITY_LIST = (
#         ('Worker', 'DepartMent Worker'),
#         ('Depart', 'DepartMent Leader'),
#         ('Center', 'Center Leader'),
#         ('Company', 'Company Leader'),
#     )
#     name = models.CharField(max_length=60,default='name')
#     identity = models.CharField(max_length=20, choices=IDENTITY_LIST,default='Worker')
#     def __str__(self):
#         return self.name


@python_2_unicode_compatible  # only if you need to support Python 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    person = models.ManyToManyField(User)
    def __str__(self):
        return self.choice_text




def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)
# class Doc(models.Model):

#     upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

