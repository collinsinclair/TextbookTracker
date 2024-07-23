from django.contrib import admin
from .models import *

models = [Author, Book, Chapter, Section, Problem]

for model in models:
    admin.site.register(model)
