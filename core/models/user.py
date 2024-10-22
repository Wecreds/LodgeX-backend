from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group,
    Permission
)
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    def jsonfield_default_value(): 
        return {"birth_date": "", "nationality": "", "street_address": "", "city":"", "state": "", "postal_code": "", "country": ""} 
    
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_("email"),
        help_text=_("Email")
        )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("name"),
        help_text=_("Username")
    )
    telephone = models.IntegerField(
        unique=True,
        verbose_name=_("telephone"),
        help_text=_("Telefone celular do usuário.")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Usuário está ativo"),
        help_text=_("Indica que este usuário está ativo.")
    )
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_permission_user_set', 
        blank=True
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Usuário é um funcionário"),
        help_text=_("Indica que este usuário é um funcionário da empresa.")    
    )
    personal_info = models.JSONField(null=True, default=jsonfield_default_value)
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta options for the model."""

        verbose_name = "User"
        verbose_name_plural = "Users"