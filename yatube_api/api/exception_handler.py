from django.http import Http404

from rest_framework.views import exception_handler
from rest_framework.exceptions import (
    NotAuthenticated,
    ValidationError,
    PermissionDenied
)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, NotAuthenticated):
        response.data = {
            'detail': 'Учетные данные не были предоставлены.'
        }
    elif isinstance(exc, PermissionDenied):
        response.data = {
            'detail': 'У вас недостаточно прав для \
            выполнения данного действия.'
        }
    elif isinstance(exc, ValidationError):
        for field, errors in exc.detail.items():
            if 'This field is required.' in errors:
                exc.detail[field] = ['Обязательное поле.']

    elif isinstance(exc, Http404):
        response.data = {
            'detail': 'Страница не найдена.'
        }
    return response
