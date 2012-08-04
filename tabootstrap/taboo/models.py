from django.db import models
from django.forms import ModelForm
from django.forms.models import modelformset_factory

class TabooWord(models.Model):
    word = models.CharField(max_length=30,unique=True)
    banned_words = models.ManyToManyField('BannedWord')
    user_created = models.BooleanField(default=False)
    
class BannedWord(models.Model):
    word = models.CharField(max_length=30,unique=True)
    
class TabooWordForm(ModelForm):
    class Meta:
        model = TabooWord
        exclude = ('banned_words')
        
class BannedWordForm(ModelForm):
    class Meta:
        model = BannedWord
        

