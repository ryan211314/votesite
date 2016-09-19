from django.contrib import admin
from .models import Question,Choice,GradeQuestion,Grade



class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

class GradeInline(admin.StackedInline):
    model = Grade
    extra = 3

class GradeQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [GradeInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(GradeQuestion, GradeQuestionAdmin)
admin.site.register(Choice)
# admin.site.register(Person)
# admin.site.register(Doc)