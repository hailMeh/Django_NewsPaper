from django.contrib.auth.forms import UserCreationForm, UserChangeForm #Берем основные классы из стандартных форм
from .models import CustomUser # импорт дополнительных полей из модели


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm): # Изменение существующего стандарта формы
        model = CustomUser  # берем новую модель
        fields = UserCreationForm.Meta.fields + ('age', ) # из модели добавляются поля по порядку


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserChangeForm.Meta.fields
