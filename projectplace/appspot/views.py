from django.shortcuts import render,redirect
from .forms import userForm, LoginForm, CategoryForm, TransactionForm
from .models import User, Transaction, Category
from django.contrib import messages
# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=userForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.role='personal'
            user.save()
            return redirect('login')
    else:
        form=userForm()
    return render(request, 'display/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == password:  # Simple check (no hash yet)
                    # Save user info in session (basic login)
                    request.session['username'] = user.username
                    if user.role=="admin":
                        return redirect('admin-home')
                    return redirect('home')  # redirect to home page
                else:
                    messages.error(request, 'Incorrect password.')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist.')
    else:
        form = LoginForm()

    return render(request, 'display/login.html', {'form': form})

def home_view(request):
    user = User.objects.get(username=request.session['username'])
    context={'username': user.username, 'balance': user.balance}
    
    return render(request,'display/home.html',context)

    
def add_categories(request):
    user = User.objects.get(username=request.session['username'])
    form=''
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            category=form.save(commit=False)
            category.totalspend = 0.00
            category.userid=user
            category.save()
            return redirect('home')
    else:
        form=CategoryForm()
    return render(request, 'display/add_category.html', {'form':form})


def add_transactions(request):
    user = User.objects.get(username=request.session['username'])
    form=''
    if request.method=='POST':
        form= TransactionForm(request.POST)
        if form.is_valid():
            transaction=form.save(commit=False)
            user.balance=user.balance-transaction.amount
            user.save()
            transaction.userid=user
            transaction.save()
            return redirect('home')
    else: 
        form=TransactionForm()
    return render(request,'display/add_transactions.html',{'form':form})

def report(request):
    user = User.objects.get(username=request.session['username'])
    transactions = Transaction.objects.filter(userid=user).order_by('-date')  # Sorted by date descending
    return render(request, 'display/report.html', {'transactions':transactions} )
