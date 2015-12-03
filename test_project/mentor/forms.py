from django import forms
from .models import Mentor
from .models import Student

class MentorForm(forms.ModelForm):
	class Meta:
		model=Mentor
		fields=['mentor_name','mentor_email','mentor_city','mentor_qualification','mentor_qualification1','mentor_qualification2','pub_date']



class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields=['name','student_name','city','email','course']