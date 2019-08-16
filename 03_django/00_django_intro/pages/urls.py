from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # url 경로 마지막에 /를 붙이는 습관
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('isitgwangbok/', views.isitgwangbok),
    path('template_language/', views.template_language),
    path('times/<int:num1>/<int:num2>/', views.times),
    path('hello/', views.hello),
    path('image/', views.image),
    path('dinner/', views.dinner),
]