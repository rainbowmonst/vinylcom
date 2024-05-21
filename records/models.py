from django.db import models

class Record(models.Model):
    artist = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    release_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genres = models.CharField(max_length=200)
    image = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return f"{self.artist} - {self.album_name} ({self.release_year})"

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.record.artist} ({self.quantity})"