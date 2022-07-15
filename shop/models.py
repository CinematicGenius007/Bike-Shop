from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Frame(color={self.color})"


class Seat(models.Model):
    color = models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Seat(color={self.color})"


class Tire(models.Model):
    type = models.CharField(max_length=40)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Tire(type={self.type})"


class Basket(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return f"Basket(quantity={self.quantity})"


class Bike(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    has_basket = models.BooleanField()
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bike(name={self.name})"

    def hasBasket(self):
        return "yes" if self.has_basket else "no"

    def place_order(self):
        bike_frame = Frame.objects.get(id=self.frame.id)
        bike_frame.quantity -= 1
        bike_frame.save()

        bike_tire = Tire.objects.get(id=self.tire.id)
        bike_tire.quantity -= 2
        bike_tire.save()

        bike_seat = Seat.objects.get(id=self.seat.id)
        bike_seat.quantity -= 1
        bike_seat.save()

        if self.has_basket:
            bike_basket = Basket.objects.filter().first()
            bike_basket.quantity -= 1
            bike_basket.save()


class Order(models.Model):
    PENDING = "P"
    READY = "R"
    ORDER_STATUS = [(PENDING, "pending"), (READY, "ready")]

    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, default=None, blank=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default=PENDING, blank=True)

    def __str__(self):
        return f"Order(name={self.name})"
