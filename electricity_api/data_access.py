from django.db.models.functions import Cast, Substr
from django.db.models import DateField, Min, Max

from electricity_api.models import Days, Months


def get_data(user_id, entity, start_date, limit):
    if entity == "days":
        return (
            Days.objects.annotate(
                timestamp=Cast(Substr("timestamp_raw", 1, 10), DateField())
            )
            .filter(timestamp__gte=start_date, user_id=user_id)
            .all()[:limit]
        )
    else:
        return (
            Months.objects.annotate(
                timestamp=Cast(Substr("timestamp_raw", 1, 10), DateField())
            )
            .filter(timestamp__gte=start_date, user_id=user_id)
            .all()[:limit]
        )


def get_limits(user_id, entity):
    if entity == "days":
        return (
            Days.objects.annotate(
                max_timestamp=Max(Cast(Substr("timestamp_raw", 1, 10), DateField())),
                min_timestamp=Min(Cast(Substr("timestamp_raw", 1, 10), DateField())),
                max_consumption=Max("consumption"),
                min_consumption=Min("consumption"),
                max_temperature=Max("temperature"),
                min_temperature=Min("temperature"),
            )
            .filter(user_id=user_id)
            .first()
        )
    else:
        return (
            Months.objects.annotate(
                max_timestamp=Max(Cast(Substr("timestamp_raw", 1, 10), DateField())),
                min_timestamp=Min(Cast(Substr("timestamp_raw", 1, 10), DateField())),
                max_consumption=Max("consumption"),
                min_consumption=Min("consumption"),
                max_temperature=Max("temperature"),
                min_temperature=Min("temperature"),
            )
            .filter(user_id=user_id)
            .first()
        )
