from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    private_item = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    posting_date = models.DateField(auto_now_add=True)