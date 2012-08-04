from django.db import models

class TabooWord(models.Model):
    word = models.CharField(max_length=30)
    banned_words = models.ManyToMany('BannedWord')
    user_created = models.BooleanField(default=False)
    
class BannedWord(models.Model):
    word = models.CharField(max_length=30)
    
