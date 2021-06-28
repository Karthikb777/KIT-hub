from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
import random

def genCode():
    src = [str(random.randint(a = 0, b = 9)) for i in range(7)]
    code = ''.join(src)
    return int(code)

# Create your models here.
class Note(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()
    uploadedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
    coverImage = models.ImageField(upload_to='images/')
    dateUploaded = models.DateTimeField(auto_now_add=True)
    impressions = models.IntegerField(default=1)
    label = models.CharField(max_length=10)
    user = models.CharField(max_length=200)
    # uniqueCode = models.IntegerField(default=genCode())

    def __str__(self):
        return self.name
    

'''
this class is used to represent a note pdf.
it will have a name, file, date added, impressions for ranking,
user who added it, and a unique code to represent it.
'''
class NotesOfUser(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.User.username



class ModRequests(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username



# class Announcements(models.Model):
#     pass

# build announcements model and build a model form
# view to add an announcement from a moderator account, edit an announcement, and deletion functionality