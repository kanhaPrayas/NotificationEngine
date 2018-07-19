from django.core.exceptions import ValidationError
import re
from .constants import VALID_TELEPHONE_STRING
from django.utils.translation import ugettext_lazy as _

# ApiCore/models.py
def tele_match(value):
    pattern = """
        ^           #Begin of the string
        [\(]?       # Possible open parenthesis
        [\+]		# Possible + char
        (\d{1,3})   # Digits for ISD code
        [\)]?       # Possible open parenthesis
        (\d{3})		#First 3 digits
        [-|.| ]?    # Possible separators
        (\d{3})   	# Second group of 3 digits
        [-|.| ]?    # Possible separators
        (\d{4,5})   # Last group of digits
        $
    """
    if not re.search(pattern, value, re.VERBOSE):
        raise ValidationError(
            _('%(value)s is not an valid phone number. '
                + 'Valid numbers are %(VALID_TELEPHONE_STRING)s'),
            params={'value': value,
                    'VALID_TELEPHONE_STRING': VALID_TELEPHONE_STRING
                    },
        )
