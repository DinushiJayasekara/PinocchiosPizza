from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from .models import Menu_Regular_Pizza, Menu_Sicilian_Pizza, Menu_Topping, Menu_Sub, Menu_Pasta, Menu_Salad, Menu_Dinner_Platter, Menu_Sub_Extra, Order, All_Order

# Create your views here.

def register(request):
    return render(request, "orders/register.html")


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})

    Extra_Sub1 = Menu_Sub.objects.filter(id=10)
    Extra_Cheese = Menu_Sub.objects.filter(id=19)
    context = {
        "user": request.user,

        "Extra_Sub1": Extra_Sub1,
        "Extra_Cheese": Extra_Cheese,
        "Menu_Regular_Pizza": Menu_Regular_Pizza.objects.all(),
        "reg1": Menu_Regular_Pizza.objects.get(id=10),
        "reg2": Menu_Regular_Pizza.objects.get(id=11),
        "reg3": Menu_Regular_Pizza.objects.get(id=12),
        "reg4": Menu_Regular_Pizza.objects.get(id=13),
        "reg5": Menu_Regular_Pizza.objects.get(id=14),
        "Menu_Sicilian_Pizza": Menu_Sicilian_Pizza.objects.all(),
        "sic1":Menu_Sicilian_Pizza.objects.get(id=1),
        "sic2":Menu_Sicilian_Pizza.objects.get(id=2),
        "sic3":Menu_Sicilian_Pizza.objects.get(id=3),
        "sic4":Menu_Sicilian_Pizza.objects.get(id=4),
        "sic5":Menu_Sicilian_Pizza.objects.get(id=5),
        "Menu_Topping": Menu_Topping.objects.all(),
        "Menu_Sub": Menu_Sub.objects.exclude(name="+ Mushrooms").exclude(name="+ Green Peppers").exclude(name="+ Onions").exclude(name="Extra Cheese on any sub"),
        "Menu_Pasta": Menu_Pasta.objects.all(),
        "pasta1":Menu_Pasta.objects.get(id=1),
        "pasta2":Menu_Pasta.objects.get(id=2),
        "pasta3":Menu_Pasta.objects.get(id=3),
        "Menu_Salad": Menu_Salad.objects.all(),
        "Menu_Dinner_Platter": Menu_Dinner_Platter.objects.all(),
        "Menu_Sub_Extra": Menu_Sub_Extra.objects.all(),
    }
    return render(request, "orders/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Oops! Invalid Credentials :( Try again"})

def logout_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]

        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    logout(request)
    return render(request, "orders/login.html", {"message": "You are currently logged out!"})

def submitOrder(request):
    if request.method == 'POST':
        username = (request.user.username)
        ordersize = request.POST["ordersize"]
        orderquantity = request.POST["orderquantity"]
        ordertype = request.POST["ordertype"]
        orderextra = request.POST.getlist('extra[]')
        ordersmallprice = request.POST["ordersmallprice"]
        orderlargeprice = request.POST["orderlargeprice"]
        orderprice = request.POST["orderprice"]
        order = Order.objects.create(username=username, size=ordersize, quantity=orderquantity, type=ordertype, extra=orderextra, smallprice=ordersmallprice, largeprice=orderlargeprice, price=orderprice)
        allorders = All_Order.objects.create(username=username, size=ordersize, quantity=orderquantity, type=ordertype, extra=orderextra, smallprice=ordersmallprice, largeprice=orderlargeprice, price=orderprice)

        context = {
            "Order": Order.objects.all(),
        }
    return HttpResponseRedirect(reverse("index"))

def finalOrder(request):
    context = {
        "Order": Order.objects.all(),
    }
    return render(request, "orders/finalOrder.html", context)

def viewOrder(request):
    context = {
        "All_Order": All_Order.objects.all(),
    }
    return render(request, "orders/viewOrder.html", context)

def sendMail(request):
    email = request.user.email
    subject = "Order Successful at Pinocchio's Pizza & Subs!!!"
    message = "Hello "+request.user.username+",\n\nWe have received your order and we will get started on your delicious meal right away!\nThank you for ordering at Pinocchio's Pizza & Subs.\nEnjoy your food :)\n\nCheers,\nPinocchio"
    from_email = settings.EMAIL_HOST_USER
    to_list = [email,settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    return HttpResponseRedirect(reverse("index"))

def clearCart(request):
    username = (request.user.username)
    print(username)
    Order.objects.filter(username=username).delete()
    return render(request, "orders/finalOrder.html")
