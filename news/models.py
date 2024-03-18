from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .send_news import send_news

class Email(models.Model):
    email = models.EmailField(blank=False, null=False)

    def __str__(self) -> str:
        return self.email

class News(models.Model):
    title = models.CharField(max_length=250, blank=False)
    body = models.TextField(blank=False)
    email = models.ForeignKey(Email, related_name='news', blank=False, on_delete=models.SET_NULL, null=True)
    sent = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        send_mail(self.title, self.body, settings.EMAIL_HOST_USER, [self.email])
        send_news(self.title, self.body, Users.objects.all())
        super(News, self).save(*args, **kwargs)

class Users(models.Model):
    tel_user_id = models.CharField(max_length=1000)        
