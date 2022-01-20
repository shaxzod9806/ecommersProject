from django.db import models

# Create your models here.

SMS_CHOISES = (
    (1, 'create_user'),
    (2, 'reset_password'),
    (3, 'notifications'),
    (4, 'news'),
)

SENT_OPTIONS = (
    (0, 'not_sent'),
    (1, 'sent'),
)


class SMS(models.Model):
    phone_number = models.CharField(max_length=13, null=True)
    text = models.TextField()
    sms_type = models.PositiveSmallIntegerField(choices=SMS_CHOISES, default=1)
    is_sent = models.PositiveSmallIntegerField(choices=SENT_OPTIONS, default=0)
