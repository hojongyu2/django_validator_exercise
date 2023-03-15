from django.db import models
from django.core import validators as valid
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

    # record_broken_date = models.DateTimeField()

def is_future(record_date):
    if record_date > timezone.now():
        raise ValidationError("Can't set record in the future.")
    
def true_false(relay):
    if relay != True or relay != False:
        raise ValidationError("'None' value must be either True or False.")
        
def is_valid_stroke(stroke):
    strings = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in strings:
        raise ValidationError("doggie paddle is not a valid stroke")

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    team_name = models.CharField(max_length=250)
    relay = models.BooleanField(default=True, validators=[true_false])
    # stroke = models.CharField(max_length=250, validators=[is_valid_stroke])
    stroke = models.CharField(max_length=250, validators=[RegexValidator(regex=r'^(front crawl|butterfly|breast|back|freestyle)$', message = "doggie paddle is not a valid stroke")])
    distance = models.IntegerField(validators=[valid.MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[is_future])
    

