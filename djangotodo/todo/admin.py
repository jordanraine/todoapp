from django.contrib import admin
from todo.models import List
from todo.models import Item

admin.site.register(List)
admin.site.register(Item)
# Register your models here.
