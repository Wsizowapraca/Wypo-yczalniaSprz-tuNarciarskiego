from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

from datetime import datetime

from .forms import RentForm, LoginForm, RegisterForm
from .models import Equipment, Rent, User

def login_view(request):
    form = LoginForm()
    message=''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('equipment')
            else:
                message='Login Failed'
    
    return render(request, 'login.html', {"message": message})

def equipment_view(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment.html', {'equipment':equipment})

def logout_view(request):
    logout(request)
    return redirect('/login')

def register_view(request):
    form = RegisterForm()
    print(request.POST)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['typeEmailX'], password=form.cleaned_data['typePasswordX'])
            new_user.save()
            return redirect('login')
            
    return render(request, 'register.html')

def rent_view(request, pk):
    eq = Equipment.objects.get(pk=pk)
    if request.method == "POST":
        form = RentForm(request.POST)
        if form.is_valid():
            new_obj = Rent.objects.create(client=request.user, rented_eq=eq, end_of_rent_date=form.cleaned_data['enddate'], phone=form.cleaned_data['phone'], email=form.cleaned_data['email'])
            new_obj.save()
            return redirect('equipment')
    else:
        form = RentForm()
    return render(request, 'rent_form.html', {'eq': eq})

def your_rents_view(request):
    your_rent = Rent.objects.filter(client=request.user)
    now = datetime.now()
    penalty = {}
    for rent in your_rent:
        rent_date = rent.end_of_rent_date.date()
        rent_time = rent.end_of_rent_date.time()
        current_date = now.date()
        current_time = now.time()
        if rent_date.day < current_date.day and rent_date.month == current_date.month:
            # penalty = {rent.id: abs((rent_date.day - current_date.day)* 15)}
            penalty[rent.id] = []
            penalty[rent.id].append(abs((rent_date.day - current_date.day)* 15))
        if rent_date.day == current_date.day and rent_date.month == current_date.month and rent_time.hour < current_time.hour:
            print('hours',rent_time.hour - current_time.hour)
            # penalty = {rent.id: abs((rent_time.hour - current_time.hour)* 2)}
            penalty[rent.id] = []
            penalty[rent.id].append(abs((rent_time.hour - current_time.hour)* 2))
    print(penalty)
    return render(request, 'your_rents.html', {"equipment": your_rent, "penalty": penalty})