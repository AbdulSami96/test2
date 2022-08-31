from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True)

class Fiction(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True)

class NonFiction(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True)

class Urdu(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True)

class Child(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True)

class Horror(models.Model):
    name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.ImageField(blank=True, null=True)
