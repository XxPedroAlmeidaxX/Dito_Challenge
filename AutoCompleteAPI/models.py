from django.db import models


class User(models.Model):

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )


class EventData(models.Model):

    event = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    dateTime = models.DateTimeField(
        null=False
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
