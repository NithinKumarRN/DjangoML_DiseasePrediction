from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Symptom, UserSymptomReport, CustomUser

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('email',)
        fields = ('username','email','password1','password2')

class SymptomReportForm(forms.Form):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def save(self, user):
        report = UserSymptomReport.objects.create(user=user)
        report.symptoms.set(self.cleaned_data['symptoms'])
        return report
# forms.py
from django import forms
from .models import Symptom

class SymptomSelectionForm(forms.Form):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
# from django import forms

# class CustomUserCreationForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        
        # try:
            # from django.contrib.auth.models import User
        # except ImportError:
            # from django.contrib.auth.models import User as User
        # self.fields['username'].queryset = User.objects.all()