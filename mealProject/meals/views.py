from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewMealForm,SignupForm, LoginForm
# Create your views here.
from .models import Meal, MealRating
from django.contrib.auth.forms import UserCreationForm

def index(request):


    all_meals = Meal.objects.all()
    breakfast = all_meals.filter(typical_mealtime=1)[:3]
    lunch = all_meals.filter(typical_mealtime=2)[:3]
    dinner = all_meals.filter(typical_mealtime=3)[:3]
    recently_added = all_meals.order_by('-date_added')[:3]
    top_rated = all_meals.order_by('-number_of_votes')[:3]

    if request.method == 'POST':

        form = NewMealForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'new meal was added')
    else:
        form = NewMealForm()

    params = {'form': form, 'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner, 'recently_added': recently_added,
              'top_rated': top_rated, 'loginform': LoginForm }
    return render(request,'meals/loading_page.html', params)


def category_list(request,typical_mealtime):

    all_meal = Meal.objects.all()
    if typical_mealtime==4:
        category_list = all_meal.order_by('-date_added')
    else:
        category_list = all_meal.filter(typical_mealtime=typical_mealtime)

    params = {'category_list': category_list }
    return render(request,'meals/category_list.html',params)


def meal_detail(request,meal_id):
    meal = Meal.objects.get(id=meal_id)


    return render(request, 'meals/meal_detail.html', {'meal': meal})


def favorite(request,meal_id,rate):
    meal = Meal.objects.get(id=meal_id)
    meal.number_of_votes +=1
    meal.save()
    meal_rate = MealRating(rating=rate,meal_id=meal_id)
    meal_rate.save()
    messages.success(request, 'rating was added')
    return redirect('meals:meal_detail',meal_id)

def signup(request):

    if request.method == 'GET':
        return render(request,'meals/signup.html',{'form': SignupForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            user.save()
            
            return redirect('meals:login')
        else:
            return render(request, 'meals/signup.html', {'form': UserCreationForm, 'error': 'password is not matched'})


def loginuser(request):

    if request.method == 'GET':
        return render(request, 'meals/login.html', {'form': LoginForm})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
        else:
            render(request, 'meals/login.html', {'form': LoginForm, 'errors': "User Does not Exists"})

        return redirect('meals:index')

def logoutuser(request):
    logout(request)
    return redirect('meals:index')