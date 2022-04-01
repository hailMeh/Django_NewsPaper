from django.contrib.auth.forms import UserCreationForm, UserChangeForm  # Берем стандартные формы
from .models import CustomUser  # импорт дополнительных полей из модели,которые хотим добавить


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):  # Изменение существующего стандарта формы
        model = CustomUser  # берем новую модель
        fields = UserCreationForm.Meta.fields + ('age', 'hairColor')  # из модели добавляются поля по порядку


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
