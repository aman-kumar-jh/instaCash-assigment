from django import forms
from datetime import date


from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'date', 'body')
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date
        
        