from django import template
from django.utils.safestring import mark_safe

from cvApp.models import *


register = template.Library()


@register.simple_tag()
def get_address():
    return mark_safe(Contacts.objects.get(pk=1).address)


@register.simple_tag()
def get_email():
    return mark_safe(Contacts.objects.get(pk=1).email)


@register.simple_tag()
def get_phone():
    return mark_safe(Contacts.objects.get(pk=1).phone)


@register.inclusion_tag('list_contact.html')
def show_social():
    social = SocialLinks.objects.all()
    return {"social": social}
