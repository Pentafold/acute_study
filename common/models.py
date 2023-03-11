from django.db import models


class WhiteLabel(models.Model):
    name = models.CharField(null=False, default='Default', max_length=50)


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    whitelabel = models.ForeignKey(WhiteLabel, default=1, on_delete=models.CASCADE)

    class Meta:
        abstract = True
