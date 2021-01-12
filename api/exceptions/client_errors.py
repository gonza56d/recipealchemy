"""Client side http error definitions."""

# Django
from django.utils.translation import gettext_lazy as _

# REST Framework
from rest_framework import status
from rest_framework.exceptions import APIException


class DuplicateObjectException(APIException):
    """Return this when django.db.IntegrityError is raised."""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Duplicate object. The object attempted to create already exists.')
    default_code = 'duplicate_object'
