from django.shortcuts import render,redirect
from .forms import userForm, LoginForm, CategoryForm, TransactionForm, userFormAdmin
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

def admin_view(request):
    return render(request, 'adm/index.html')

def admin_users(request):
    users = User.objects.all().order_by('-uid')  # Get all users ordered by newest first
    return render(request, 'adm/adminusers.html', {'users': users})

def admin_transactions(request):
    transaction = Transaction.objects.all()
    return render(request, "adm/admintransaction.html", {'transactiondata' : transaction})

def admin_categories(request):
    return render(request, 'adm/admincategory.html')

def userlist(request):
    search_query = request.GET.get('search', '')
    if search_query:
        user = User.objects.filter(username__icontains=search_query)
    else:
        user = User.objects.all()
    return render(request, "adm/userlist.html",{'users': user})


def insertuser(request):
    if request.method == 'POST':
        try:
            #vuid = request.POST['uid']
            vfirst = request.POST['first']
            vlast = request.POST['last']
            vusername = request.POST['username']
            vemail = request.POST['email']
            vpassword = request.POST['password']
            vbalance = request.POST['balance']
            vrole= request.POST['role']
            # Check if user ID already exists
            if User.objects.filter(username=vusername).exists():
                messages.error(request, 'User with this Name already exists!')
                return redirect('userreg')
                
            # Create and save new user
            user=User(first=vfirst, last=vlast, username=vusername, email=vemail, password=vpassword, balance=vbalance, role=vrole) 
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('admin-users')
            
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('userreg')
     

def userreg(request):
    return render(request, 'adm/userreg.html')

def deleteprofile(request, id):
    x = User.objects.filter(uid=id)
    x.delete()
    return redirect("/userlist")


def viewtransaction(request):
    transaction = Transaction.objects.all()
    return render(request, "adm/viewtransaction.html", {'transactiondata' : transaction})


def categoryreg(request):
    return render(request, 'adm/categoryreg.html', {}) 

def updateprofile(request, uid):
    if request.method=='POST':
        try:
            user=User.objects.get(uid=uid)
            user.first = request.POST['first']
            user.last = request.POST['last']
            user.username = request.POST['username']
            user.email = request.POST['email']
            new_password = request.POST['password']
            if new_password:
                user.password = new_password
            user.balance = request.POST['balance']
            user.save()
            messages.success(request, 'Successfully Updated')
            return redirect('/userlist')
        except User.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('/userlist')
        except Exception as e:
            messages.error(request, f'Error in updating: {str(e)}')
            return redirect('/userlist')
        
    return redirect('/userlist')

def useredit(request, id):
    y = User.objects.get(uid=id)
    return render(request,"adm/useredit.html", {'user':y})

def insertcategory(request):
    if request.method == 'POST':
        vcname = request.POST[ 'cname' ]
        vcset_budget = request.POST[ 'cset_budget']
        vcspend = request.POST[ 'cspend' ]
        vcusername = request.POST[ 'cusername' ]
        if Category.objects.filter(userid=vcname).exists():
            messages.error(request, 'Category with this Name already exists!')
            return redirect('categoryreg')
        
        cat=Category(name=vcname, setbudget=vcset_budget, totalspend=vcspend, userid=vcusername)
        cat.save()
        messages.success(request, 'Category registered successfully!')
        return redirect('dashboard-category')


def categorylist(request):
    cat=Category.objects.all()
    return render(request, 'adm/categorylist.html', {'category':cat})

def updatecategory(request, catid):
    if request.method=='POST':
        try:
            cat=Category.objects.get(catid=catid)
            cat.name= request.POST['cname']
            cat.setbudget = request.POST['cset_budget']
            cat.totalspend = request.POST['cspend']
            cat.userid = request.POST['cusername']
            cat.save()
            return redirect('/categorylist')
        
        except Category.DoesNotExist:
            messages.error('Category not found')
            return redirect(request, '/categorylist')
            
    return redirect('/categorylist')

def categoryedit(request, catid):
    z = Category.objects.get(catid=catid)
    return render(request,"adm/categoryedit.html", {'category' : z})

    