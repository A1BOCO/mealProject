from django.forms import ModelForm,Textarea
from .models import MealRecommend
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class NewMealRecommendForm(ModelForm):
    class Meta:
        model = MealRecommend
        fields = ['name', 'image_url', 'description', 'country_of_origin', 'tags', 'description']
        widgets = {
            'description' : Textarea(attrs={'cols': 40, 'rows': 10})
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs['class'] = 'form-control'
        self.fields['tags'].widget.attrs['multiple'] = 'multiple'
        self.fields['tags'].widget.attrs['class'] = 'js-example-basic-multiple form-control'
        self.fields['tags'].widget.attrs['name'] = 'states[]'

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