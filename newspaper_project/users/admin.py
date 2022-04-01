from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Берется стандартная админская панель

# Register your models here.

from .forms import CustomUserChangeForm, CustomUserCreationForm  # Импорт двух измененных от стандарта форм
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'age', 'username', 'is_staff', 'hairColor', ]  # Отображаемые поля в админке , 'age' - новое


admin.site.register(CustomUser, CustomUserAdmin)
