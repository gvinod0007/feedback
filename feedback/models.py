from django.db import models
from django.contrib.auth.hashers import make_password

class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords only

    class Meta:
        db_table = 'feedback_customer'  # Set the table name here

    def save(self, *args, **kwargs):
        if self.pk is None:  # Only hash if the object is being created
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username







# class Customer(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)  # Store plain-text passwords

#     class Meta:
#         db_table = 'feedback_customer'  # Set the table name here

#     def save(self, *args, **kwargs):
#         # Save without hashing the password
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.username

