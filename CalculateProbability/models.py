from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.core.exceptions import ValidationError

#validation method to check if the user selects a die of 0 sides

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            'A die has no face ???',
            params={'value': value},)

#Create the model to input the number of sides
class Input(models.Model):
    Numsides = models.PositiveIntegerField(validators=[validate_nonzero], default=1)



class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = "__all__"
