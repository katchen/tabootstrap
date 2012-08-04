from django.core.management.base import BaseCommand, CommandError
import random
import os.path
from django.core.files import File
from taboo.models import TabooWord, BannedWord
from tabootstrap import settings
from django.db import transaction

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

class Command(BaseCommand):
    args = ''
    help = 'make a fake database [TESTING ONLY]'  

    @transaction.commit_manually    
    def handle(self, *args, **options):
        print("Stay calm this is going to take a while.")
        print("Deleting Everything:")
        try:
            BannedWord.objects.all().delete()
            TabooWord.objects.all().delete()
        except:
            print("yes")
        print("Generating new db...")
        path = os.path.dirname(SITE_ROOT)
        path = os.path.dirname(path)
        path = os.path.dirname(path)
        FILE = open(path+"/wordlist.txt", "r")
        
        lines = FILE.readlines()
        for line in lines:
            line = line.replace("\n","")
            taboo_word = line.split(':')[0]
            banned_words = line.split(':')[1].split(',')
            taboo_exist = TabooWord.objects.filter(word=taboo_word)
            if taboo_exist:
                continue
            else:
                model = TabooWord.objects.create(word=taboo_word)
            print(taboo_word)
            print(banned_words)
            for banned_word in banned_words:
                exists = BannedWord.objects.filter(word=banned_word)
                if exists:
                    banned_model = exists[0]
                else:
                    banned_model = BannedWord.objects.create(word=banned_word)
                if not model.banned_words.filter(word=banned_word):
                    model.banned_words.add(banned_model)
        print("Complete")
        transaction.commit()

