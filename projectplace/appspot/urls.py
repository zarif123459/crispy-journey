from django.urls import path
from .views import signup_view,login_view,home_view,add_categories,add_transactions,report

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home_view,name='home'),
    path('category_create/', add_categories, name='category_create' ),
    path('transaction_create/', add_transactions, name='transaction_create'),
    path('report/', report, name='report'),
    ]

