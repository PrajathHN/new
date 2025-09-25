from django.urls import path
from lawfirmapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('about',views.about,name='about'),
    path('allCases',views.allCases,name='allCases'),
]