from django.contrib import admin
from .models import Note, NotesOfUser, ModRequests
# Register your models here.

admin.site.register(Note)
admin.site.register(NotesOfUser)
admin.site.register(ModRequests)