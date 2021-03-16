#!/usr/bin/env python
# (c) 2017 CJ Associates
#
from django.core.exceptions import ValidationError

def small_integer_only(value):
    if not 0 <= value <= 10:
        raise ValidationError("value must be between 0 and 10")
