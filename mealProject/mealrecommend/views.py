
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.views.generic import CreateView

from .forms import NewMealRecommendForm,SignupForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import MealRecommend, MealRecommendTag, MealRecommendRating


def index(request):
    if request.method == "GET":
        all_meals = MealRecommend.objects.all()
        tags = MealRecommendTag.objects.all()
        contents = {'meals': all_meals,
                    'tags': tags,
                    }
        return render(request,'mealrecommend/landing_page.html', contents)
    else:

        all_meals = MealRecommend.objects.filter(tags__in=request.POST.getlist('tags'))
        taglist = [int(i) for i in request.POST.getlist('tags')]
        tags = MealRecommendTag.objects.all()
        contents = {'meals': all_meals,
                    'tags': tags,
                    'ids' : taglist,
                    }
        return render(request,'mealrecommend/landing_page.html', contents)





def add_meal(request):
    if request.method == 'GET':
        form = NewMealRecommendForm()

        contents = {
            'form' : NewMealRecommendForm()
                    }
        return render(request,'mealrecommend/meal_add.html', contents)
    else:
        form = NewMealRecommendForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            print(form)
            new_meal = form.save(commit=False)
            new_meal.user = request.user
            new_meal.save()
            messages.info(request, 'New meal was added')

        return redirect('mealrecommend:index')

def signup(request):
    if request.method == 'GET':
        return render(request, 'meals/signup.html', {'form': SignupForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()

            return redirect('meals:login')
        else:
            return render(request, 'meals/signup.html', {'form': UserCreationForm, 'error': 'password is not matched'})


def loginuser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            print(" login user")
        else:
            print("user is not logged in")

        # redirect to original page
        return redirect(request.META['HTTP_REFERER'])


def logoutuser(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])


def history(request):
    yourRating = MealRecommendRating.objects.filter(user=request.user)

    return render(request,'mealrecommend/history.html',yourRating)


def meal_detail(request,meal_id):
    meal = MealRecommend.objects.get(id=meal_id)


    return render(request, 'mealrecommend/meal_detail.html', {'meal': meal})

def favorite(request,meal_id,rate):
    meal = MealRecommend.objects.get(id=meal_id)
    meal.number_of_votes +=1
    meal.save()
    meal_rate = MealRecommendRating(rating=rate,meal_id=meal_id)
    meal_rate.save()
    messages.success(request, 'rating was added')
    return redirect('mealrecommend:meal_detail',meal_id)