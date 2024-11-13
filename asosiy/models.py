from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Turi(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kim = models.ForeignKey(Turi, on_delete=models.CASCADE)
    ozi_haqida = models.TextField()

    def __str__(self):
        return self.kim.name


class Tajriba(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kompaniya = models.CharField(max_length=200)
    yil = models.CharField(max_length=200)
    kim = models.ForeignKey(Turi, on_delete=models.CASCADE)

    def __str__(self):
        return self.kim.name


class Malaka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nomi = models.ForeignKey(Category, on_delete=models.CASCADE)
    daraja = models.IntegerField()

    def __str__(self):
        return self.nomi.name


class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link1 = models.URLField(max_length=200)
    link2 = models.URLField(max_length=200,  null=True, blank=True)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return f"Message from {self.name}"