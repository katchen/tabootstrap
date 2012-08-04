from django.db import models

class TabooWord(models.Model):
    word = models.CharField(max_length=30,unique=True)
    banned_words = models.ManyToManyField('BannedWord')
    user_created = models.BooleanField(default=False)

    def __unicode__(self):
        return self.word
    
class BannedWord(models.Model):
    word = models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return self.word
    
