from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("submitOrder", views.submitOrder, name="submitOrder"),
    path("finalOrder", views.finalOrder, name="finalOrder"),
    path("viewOrder", views.viewOrder, name="viewOrder"),
    path("sendMail", views.sendMail, name="sendMail"),
    path("clearCart", views.clearCart, name="clearCart")
]
