from django.contrib import admin
from .models import Article, Comment
# Register your models here.


class CommentInline(admin.TabularInline):  # Отображение модели Comment в столбик
    model = Comment
    extra = 0  # Указание дополнительных полей для отображения, по умолчанию - 3


class ArticleAdmin(admin.ModelAdmin):  # Массив внутри которого будут все классы с измененным отображением
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)  # Первым параметром основная модель в админку, вторым измененная
admin.site.register(Comment)
