
from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.base_user import BaseUserManager
from mptt.models import MPTTModel, TreeForeignKey

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin, MPTTModel):
    REPRESENTATIVE = 'SR'
    OFFICER = 'SO'
    MANAGER = 'SM'
    AREA_MANAGER = 'AM'

    EMPLOYEE_TYPES = (
        (REPRESENTATIVE, 'sales representative'),
        (OFFICER, 'sales officer'),
        (MANAGER, 'sales manager'),
        (AREA_MANAGER, 'area manager')
    )

    email = models.EmailField(_('email address'), null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    code = models.IntegerField(blank=True, null=True, unique=True)
    role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES, null=True)
    date_joined = models.DateField(_('date joined'), auto_now_add=False, null=True)
    date_expire = models.DateField(_('date expire'), auto_now_add=False, null=True)
    avatar = models.ImageField(upload_to='static/avatars/',default='static/avatars/default.jpg', null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(default=False)

    # manager = models.ForeignKey('self', null=True, related_name='user', on_delete=models.DO_NOTHING)
    parent = TreeForeignKey('self', null=True, related_name='user', on_delete=models.DO_NOTHING)

    objects = UserManager()

    USERNAME_FIELD = 'code'
    REQUIRED_FIELDS = ['email','role','is_admin']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_adduser(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return format(self.code)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin    
