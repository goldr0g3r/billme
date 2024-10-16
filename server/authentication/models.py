from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from authentication.manager import UserManager

# Create your models here.

USER_ROLES = [
    ("biller", "Biller"),
    ("owner", "Owner"),
    ("admin", "Admin"),
    ("salesman", "Salesman"),
]


class User(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(
        _("role"), max_length=10, choices=USER_ROLES, default="salesman"
    )
    email = models.EmailField(_("email address"), unique=True)
    username = None
    first_name = models.CharField(_("first name"), max_length=30)
    last_name = models.CharField(_("last name"), max_length=30)

    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    def __str__(self):
        return self.email
