from django import forms
from .models import Subject, Question


class QuestionForm(forms.ModelForm):
    #Form for question and answer
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topic = Subject.objects.all()
        choice = [(s.id, s.friendly_name) for s in topic]

        self.fields['subject'].choices = choice
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'profile-form-input mb-2'