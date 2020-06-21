from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request, "index.html")

def process_money(request):
    if request.method == "POST":
        income = request.POST.get('type')
        if income == 'farm':
            coins = random.randint(10, 20)
            request.session['gold'] += coins
            request.session['log'].insert(0, f"You gained {coins} coins.")
        elif income == 'cave':
            coins = random.randint(5, 10)
            request.session['gold'] += coins
            request.session['log'].insert(0, f"You gained {coins} coins in the cave.")
        elif income == 'home':
            coins = random.randint(2, 5)
            request.session['gold'] += coins
            request.session['log'].insert(0, f"You gained {coins} coins in your house.")
        elif income == 'casino':
            coins = random.randint(-50, 50)
            request.session['gold'] += coins
            if coins >= 0:
                request.session['log'].insert(0, f"You just won {coins} coins at the casino.")
            else:
                request.session['log'].insert(0, f"You just lost {coins} coins at the casino.")
    return redirect("/")

def reset(request):
    request.session['gold'] = 0
    request.session['log'] = []
    return redirect('/')