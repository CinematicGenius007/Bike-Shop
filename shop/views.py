from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from .models import Bike, Order
from .forms import OrderForm


def index(request: HttpRequest):
    return HttpResponse("<h1>This page is under construction.</h1>")


def bikes(request: HttpRequest):
    if request.method == "GET":
        return render(request, 'bikes.html', {"bikes": Bike.objects.all()})


def bike(request: HttpRequest, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'bikeDetail.html', {'bike': Bike.objects.get(id=kwargs.get('pk'))})
    elif request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            saved_form = order_form.cleaned_data
            requested_bike = Bike.objects.get(id=kwargs.get('pk'))
            new_order = Order.objects.create(
                bike=requested_bike,
                name=saved_form.get('name'),
                surname=saved_form.get('surname'),
                phone_number=saved_form.get('phone_number'),
                status=Order.PENDING,
            )

            # This is the most important line.
            requested_bike.place_order()

            return redirect(f'/order/{new_order.id}/')
        return HttpResponseBadRequest("Please fill the form one more time, "
                                      "there has been some issue with your data.")


def order(request: HttpRequest, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'orderDetail.html', {'order': kwargs.get('pk')})
