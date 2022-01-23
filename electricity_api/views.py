import logging

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseServerError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from electricity_api.utils import string_to_date
from electricity_api.data_access import get_data, get_limits
from electricity_api.serializers import DaysSerializer, MonthsSerializer


logger = logging.getLogger(__name__)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def handle_get_data(request):
    params, error = validate_request(request)
    if error:
        return HttpResponseBadRequest(error)
    try:
        if params["entity"] == "days":
            serializer = DaysSerializer(
                get_data(
                    request.user.id,
                    params["entity"],
                    params["start_date"],
                    params["limit"],
                ),
                many=True,
            )
        else:
            serializer = MonthsSerializer(
                get_data(
                    request.user.id,
                    params["entity"],
                    params["start_date"],
                    params["limit"],
                ),
                many=True,
            )
        return JsonResponse({"data": serializer.data}, safe=False)
    except Exception as e:
        logger.error(str(e))
        return HttpResponseServerError(str(e))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def handle_get_limits(request):
    try:
        result = {
            "days": frame_limits_response(get_limits(request.user.id, "days")),  # did not have time to think about custom querysets using Django Rest framework
            "months": frame_limits_response(get_limits(request.user.id, "months")),  # Hence did not use serialisers here
        }
        return JsonResponse({"limits": result})
    except Exception as e:
        logger.error(str(e))
        return HttpResponseServerError(str(e))


def frame_limits_response(data):
    return {
        "temperature": {
            "minimum": data.min_temperature,
            "maximum": data.max_temperature,
        },
        "consumption": {
            "minimum": data.min_consumption,
            "maximum": data.max_consumption,
        },
        "timestamp": {"minimum": data.min_timestamp, "maximum": data.max_timestamp},
    }


def validate_request(request):
    try:
        params = {
            "start_date": string_to_date(request.GET["start"], "%Y-%m-%d"),
            "limit": int(request.GET["count"]),
            "entity": request.GET["resolution"],
        }
        return params, None
    except KeyError:
        return (
            {},
            "One or more query params are missing. start, count, resolution are required. Could not fetch data...",
        )
    except Exception as e:
        return {}, "Invalid format for one or more parameters"
