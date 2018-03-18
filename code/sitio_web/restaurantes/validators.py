from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy

def valida_codigo_postal(value):
   if value < 10000 or value > 99999:
        raise ValidationError('%s El valor introducido no es un código postal' % value)