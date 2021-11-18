from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import GolfGroup
from django.forms import ModelForm


# WIDGETS
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['name', 'location', 'img', 'bio', 'handicap', 'favorite_course']



def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg



class GroupForm(forms.ModelForm):
    class Meta:
        model = GolfGroup
        fields = ['golf_course', 'tee_date', 'tee_time', 'description', 'game_type']
        widgets = {
            'tee_date' : DateInput(),
            'tee_time' : TimeInput(format='%H:%M'),
            'description' : forms.Textarea(attrs={'cols': 40, 'rows': 10})
        }

# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = '__all__'
#         widgets = {
#             'my_date': DateInput()
#         }


        


