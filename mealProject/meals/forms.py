from django.forms import ModelForm,Textarea
from .models import Meal
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class NewMealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'image_url', 'description', 'country_of_origin', 'typical_mealtime', 'description']
        widgets = {
            'description' : Textarea(attrs={'cols': 40, 'rows': 10})
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control my-2'


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['id'] = 'form3Example1c'

class LoginForm(AuthenticationForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'