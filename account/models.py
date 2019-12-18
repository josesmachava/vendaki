from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from price import settings


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_regex = RegexValidator(regex=r'^\+?258?\d{9,13}$',
                                 message="O número de telefone deve ser digitado no formato: '+258849293949'. São permitidos até 13 dígitos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)  # validators should be a list

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Type(models.Model):
    name = models.CharField(max_length=30, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=30, blank=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commercial_name = models.CharField(max_length=30, blank=False, unique=False)
    company_logo = models.ImageField(upload_to='company_logo/', default='company_logo/default.jpg')
    address = models.CharField(max_length=30, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, unique=False, default=1)
    created_date = models.DateTimeField(default=timezone.now)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Referral(models.Model):
    referral_token = models.CharField(max_length=4, blank=False, default=get_random_string(length=32), editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class ReferralLink(models.Model):
    link = models.URLField()
    name = models.CharField(max_length=30, blank=True)
    referral = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
