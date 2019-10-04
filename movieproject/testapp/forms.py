from django import forms
from testapp.models import Movie
class MovieForm(forms.ModelForm):
	
	class Meta:
		model=Movie
		fields=['rdate','moviename','hero','heroine','rating']