from django.db import models
from datetime import datetime

class Contact(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  number = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.number


class Donate(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  number = models.CharField(max_length=100)
  amount = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  
  def __str__(self):
    return self.number