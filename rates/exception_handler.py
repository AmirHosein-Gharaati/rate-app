from django.core.exceptions import ValidationError as DjangoValidationError, PermissionDenied
from django.http import Http404
from rest_framework.response import Response

from rest_framework.views import exception_handler
from rest_framework import exceptions, status
from rest_framework.serializers import as_serializer_error


def drf_default_with_modifications_exception_handler(exc, ctx):
    if isinstance(exc, DjangoValidationError):
        exc = exceptions.ValidationError(as_serializer_error(exc))

    if isinstance(exc, Http404):
        exc = exceptions.NotFound()

    if isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    response = exception_handler(exc, ctx)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        return Response(
            {
                "detail": str(exc).replace('"', "'"),
                "type": type(exc).__name__,
                "message": "An unexpected error occurred."
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if isinstance(exc.detail, (list, dict)):
        response.data = {
            "detail": response.data
        }

    return response
