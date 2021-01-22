"""Client side http error declarations."""

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


class MissingFieldException(APIException):
    """Return this when django.db.IntegrityError is raised."""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Missing a required field.')
    default_code = 'required_field'

    def __init__(self, field):
        super().__init__(_(f'{field}: This field is required.'))


class MethodNotAllowedException(APIException):
    """Return this when client tried to perform a method that is not allowed for the view."""

    status_code = status.HTTP_405_METHOD_NOT_ALLOWED
    default_detail = _('This method is disabled for this resource.')
    default_code = 'method_not_allowed'
