from django import forms
from .models import College
from .models import Rating
class CollegeForm(forms.ModelForm):
	class Meta:
		model=College
		fields=['college_text','pub_date']

		
class RatingForm(forms.ModelForm):
	class Meta:
		model=Rating
		fields=['college','rating','views']