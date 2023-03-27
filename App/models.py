from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.PositiveIntegerField(null=True)
    message = models.TextField()
    phone_number = models.CharField(max_length=25, null=True)
    job = models.CharField(max_length=5, null=True)
    SITUATION = (("Pending", "Pending"),
                 ("Approved", "Approved"),
                 ("Disapproved", "Disapproved"),)
    situation = models.CharField(max_length=100, null=True, choices=SITUATION, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name
