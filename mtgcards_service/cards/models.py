from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Card(models.Model):
    name = models.CharField(max_length=200)
    local_path = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Purchases(models.Model):
    query = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_local_path = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user) + ' - ' + str(self.query)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.PositiveIntegerField(default=1000)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return str(self.user) + ' - ' + str(self.money)
