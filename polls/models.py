# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import Permission,User
from django.db.models import Avg,Max
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
    class Meta:
        verbose_name = u"问题"
        verbose_name_plural = u"问题"
    def save(self,*args,**kwargs):
        print 'save question'
        super(Question,self).save(*args,**kwargs)


class LimitQuestion(Question):
    stop_date = models.DateField('结束时间')
    def was_available(self):
        return timezone.now() > self.stop_date



class GradeQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    person = models.ManyToManyField(User)
    def __str__(self):        
        return self.question_text

class Grade(models.Model):
    question = models.ForeignKey(GradeQuestion, on_delete=models.CASCADE,related_name="pgrade",related_query_name="pgrade")
    grade = models.IntegerField(default=0)
    person = models.ManyToManyField(User,default=None)
    def __str__(self):
        return str(self.grade)


class PersonGroup(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(User,through='Membership')
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(User,on_delete=models.CASCADE)
    group = models.ForeignKey(PersonGroup,on_delete=models.CASCADE)
    date_joined = models.DateField()
    def __str__(self):
        return self.person.username + '-'+self.group.name


class CommonInfo(models.Model):
    title = models.CharField(max_length=100)
   
    class Meta:
        abstract = True

class NewsMessage(CommonInfo):
    news = models.CharField(max_length=200)




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
@python_2_unicode_compatible  # only if you need to support Python 2
class DocType(models.Model):
    typename = models.CharField(max_length=200)
    def __str__(self):

        return self.typename    
@python_2_unicode_compatible  # only if you need to support Python 2
class Doc(models.Model):

    upload = models.FileField(upload_to='uploads/')
    doctype = models.ManyToManyField(DocType)
    is_activated = models.BooleanField('是否使用',default=False)

    def __str__(self):

        return self.upload.url




