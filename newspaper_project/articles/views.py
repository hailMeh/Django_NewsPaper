from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


class ArticleListView(LoginRequiredMixin, ListView):  # Миксин не дает гостю зайти на url просмотра сообщений
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'  # Редирект на url, если гость неавторизован


class ArticleDetailView(LoginRequiredMixin, DetailView):  # Миксин не дает гостю зайти на url просмотра сообщения
    model = Article
    template_name = 'article_details.html'
    login_url = 'login'  # Редирект на url, если гость неавторизован


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                        UpdateView):  # Миксин не дает гостю зайти на url редактирования сообщений
    model = Article
    template_name = 'article_edit.html'
    fields = ['title', 'body']
    login_url = 'login'  # Редирект на url, если гость неавторизован

    def test_func(self):  # Не дает изменить сообщение, если оно не своё
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # Миксин не дает гостю зайти на url удаления сообщения
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'  # Редирект на url, если гость неавторизован

    def test_func(self):  # Не дает удалить сообщение, если оно не своё, работает благодаря миксину UserPassesTestMixin
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):  # Миксин не дает гостю зайти на url создания сообщения
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body')  # Добавлялось еще поле Author, но внизу метод def_valid ...
    login_url = 'login'  # Будет редирект на login, если пользователь не авторизован

    def form_valid(self, form):  # ... автоматически добавляет авторизованного юзера в поле authors
        form.instance.author = self.request.user
        return super().form_valid(form)
