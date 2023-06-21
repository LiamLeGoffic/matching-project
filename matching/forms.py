from django import forms
from matching.models import User, Skill, Mission, Consultant, Requirement


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('password', 'role',)
