from django.db import models

# Create your models here.

class Fundraiser(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)  # when was the record created
    updated_at = models.DateTimeField(auto_now=True)  # when was the last time the record was updated

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'fundraisers'

class Donation(models.Model):
    fundraiser = models.ForeignKey(Fundraiser, on_delete=models.CASCADE,related_name='donations')
    project_name = models.CharField(max_length=255)
    amount = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fundraiser.first_name} {self.project_name} {self.amount}"

    class Meta:
        db_table = 'donations'















