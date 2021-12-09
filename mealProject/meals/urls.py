from django.urls import path, include

from . import views

app_name = 'meals'

urlpatterns = [
    path('', views.index, name='index'),
    path('category_list/<int:typical_mealtime>', views.category_list, name='category_list'),
    path('meal_detail/<int:meal_id>', views.meal_detail, name='meal_detail'),
    path('favorite/<int:meal_id>/<int:rate>', views.favorite, name='favorite'),
    path('login/', views.loginuser, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logoutuser, name='logout'),
]
