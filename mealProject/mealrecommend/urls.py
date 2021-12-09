from django.urls import path, include

from . import views,context_processor

app_name = 'mealrecommend'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logout'),
    path('meal_detail/<int:meal_id>', views.meal_detail, name='meal_detail'),
    path('favorite/<int:meal_id>/<int:rate>', views.favorite, name='favorite'),
]
