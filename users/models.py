from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager
from common.models import WhiteLabel

class BaseUser(AbstractBaseUser, PermissionsMixin):
    """
    User model derived from Abstract base user model,
    should be able to authenticate using username and email
    """

    username = models.CharField(
        _('username'),
        max_length=254,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(default="", null=True,blank=True, max_length=50)
    last_name = models.CharField(default="", null=True,blank=True, max_length=50)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_email_verified = models.BooleanField(default=False)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        return self.username

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.username

    class Meta:
        abstract = True


class User(BaseUser):
    """
        Users model is an extension to django user model.
        Extra user fields are managed via this model
    """
    mobile_number = models.CharField(null=True, blank=True, max_length=50)
    company_name = models.CharField(null=True, blank=True, max_length=50)
    designation = models.CharField(null=True, blank=True, max_length=50)
    nationality = models.CharField(null=True, blank=True, max_length=50)

    address = models.CharField(null=True, blank=True, max_length=50)
    state = models.CharField(null=True, blank=True, max_length=50)
    city = models.CharField(null=True, blank=True, max_length=50)
    country = models.CharField(null=True, blank=True, max_length=50)

    whitelabel = models.ForeignKey(WhiteLabel, default=1, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.email

    def save(self, *args, **kwargs):
        """
            Save the user to data base.
        :param args:
        :param kwargs:
        :return:
        """
        self.full_clean()
        return super(User, self).save(*args, **kwargs)