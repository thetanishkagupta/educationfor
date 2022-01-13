from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from courseshop.models import Order
from courseshop.models import extendeduser
from django.contrib.auth  import authenticate,logout
from django.contrib.auth import login as auth_login
def home(request):
    return render(request,'home.html')
def handelLogout(request):
    logout(request)
    return redirect('logout1')
def logout1(request):
    return render(request,'logout.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['user name']
        email=request.POST['email']
        fname=request.POST['first name']
        lname=request.POST['last name']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        Phone=request.POST['phone']
        dob=request.POST['dob']
        address=request.POST['address']

        if (pass1 == pass2):
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username already taken.Please try again")
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, "Email Already Registered.Please try again")
                return redirect('signup')
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name= fname
                myuser.last_name= lname
                myuser.save()
                tanishka = extendeduser(phone_num =Phone,addre=address,dob=dob,user=myuser)
                tanishka.save()
                messages.success(request, "Registered Successfully, Please Login...!")
                return redirect('login')

        else:
            messages.error(request, "Password mismatch.Please try again")
            return redirect('signup')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Successfully Logged In.")
            if request.user.is_authenticated:
                return redirect("welcome")


        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")

    return render(request,'login.html')


    return HttpResponse("login")
def buy(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        course=request.POST['course']
        order=Order(name=name, email=email, phone=phone,address=address,course=course,user1=request.user)
        order.save()
        messages.success(request, "Congratulations! You have successfully purchased the course.")
    return render(request,'buy.html')
def profile(request):
    return render(request,'profile.html')
def welcome(request):
    return render(request,'welcome.html')
def course(request):
    log_user = request.user
    order1 = Order.objects.filter(user1 = log_user)
    return render(request,'course.html',{'order1' : order1})
