from django import template
from main.models import Note
from django.contrib.auth.models import Group


register = template.Library()

@register.filter(name='userInGrp')
def userInGrp( user, grpName ):
    grp = Group.objects.get(name=grpName)
    return True if grp in user.groups.all() else False
