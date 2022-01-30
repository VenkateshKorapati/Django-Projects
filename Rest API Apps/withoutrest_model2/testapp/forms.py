from django import forms

from testapp.models import Student
class StudentForm(forms.ModelForm):
    
    def clean_marks(self):
        inputmarks=self.cleaned_data['marks']
        if inputmarks<35:
            raise forms.ValidationError('The min marks should be above 35')
        return inputmarks
    
    class Meta:
        model=Student
        fields='__all__'
 