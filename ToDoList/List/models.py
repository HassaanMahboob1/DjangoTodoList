from django.db import models


class Item(models.Model):
    choice = (
        ("COMPLETE", "Complete"),
        ("INCOMPLETE", "Incomplete"),
    )
    item = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=choice, default="Incomplete")

    def __str__(self):
        return self.item
