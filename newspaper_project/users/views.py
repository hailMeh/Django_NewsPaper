from django.views.generic import CreateView  # Класс для создания формы
from .forms import CustomUserCreationForm  # Импорт измененной модели создания формы
from django.urls import reverse_lazy  # Редирект при успешном сабмите в переданный аргумент(url)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
