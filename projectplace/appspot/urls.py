from django.urls import path
from .views import signup_view,login_view,home_view,add_categories,add_transactions,report,admin_view,admin_users,admin_transactions,admin_categories,insertuser,userreg,userlist,viewtransaction,categoryreg,useredit,updateprofile,deleteprofile,insertcategory,categorylist,categoryedit,updatecategory,balance_sheet

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('admin-home/',admin_view,name='admin-home'),
    path('home/', home_view,name='home'),
    path('category_create/', add_categories, name='category_create' ),
    path('transaction_create/', add_transactions, name='transaction_create'),
    path('report/', report, name='report'),
    path('admin-users/', admin_users, name='admin-users'),
    path('admin-transactions/', admin_transactions, name='admin-transactions'),
    path('admin-categories/', admin_categories, name='admin-categories'),
    path('insertuser/', insertuser, name='insertuser'),
    path('userreg/', userreg, name='userreg'),
    path('userlist/', userlist, name='userlist'),
    path('viewtransaction/', viewtransaction, name='dashboard-transaction'),
    path('categoryreg/', categoryreg, name='categoryreg'),
    path('useredit/<int:id>', useredit, name='useredit'),
    path('categoryreg/', categoryreg, name='categoryreg' ),
    path('updateprofile/<int:uid>', updateprofile, name='updateprofile'),
    path('deleteprofile/<int:uid>', deleteprofile, name='deleteprofile'),
    path('categorylist/', categorylist, name='categorylist'),
    path('insertcategory/', insertcategory, name='insertcategory'),
    path('categoryedit/<int:catid>',categoryedit,name= 'categoryedit'),
    path('updatecategory/<int:catid>', updatecategory, name='updatecategory'),
    path('balancesheet/',balance_sheet,name="balancesheet" ),
    ]

