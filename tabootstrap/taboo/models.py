from django.db import models

class TabooWord(models.Model):
    word = models.CharField(max_length=30,unique=True)
    banned_words = models.ManyToManyField('BannedWord')
    user_created = models.BooleanField(default=False)
    
class BannedWord(models.Model):
    word = models.CharField(max_length=30,unique=True)
    
