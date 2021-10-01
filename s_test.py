import django

from accounts.models import CustomUser

django.setup()


CustomUser.objects.all().update(y_coin=100)
