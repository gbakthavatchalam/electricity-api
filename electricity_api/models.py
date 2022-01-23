from django.db import models


class Days(models.Model):
    class Meta:
        db_table = "days"

    day_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    timestamp_raw = models.TextField(db_column="timestamp")
    consumption = models.IntegerField()
    temperature = models.IntegerField()


class Months(models.Model):
    class Meta:
        db_table = "months"

    month_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    timestamp_raw = models.TextField(db_column="timestamp")
    consumption = models.IntegerField()
    temperature = models.IntegerField()
