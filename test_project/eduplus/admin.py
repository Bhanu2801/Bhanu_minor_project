from django.contrib import admin
from .models import Question,Choice
from .forms import QuestionForm
# Register your models here.\
#class ChoiceInline(admin.TabularInline):
 #	model=Choice
 #	extra=3
class QuestionAdmin(admin.ModelAdmin):
	fieldsets=[
		('Enter Question',{'fields':['question_text']}),
		('Date Info',{'fields':['pub_date'],'classes':['collapse']}),

	]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
#	inlines=[ChoiceInline]
	#check
	form=QuestionForm

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)