from django.urls import path
from .views import signup_view,login_view,home_view

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home_view,name='home')
]
