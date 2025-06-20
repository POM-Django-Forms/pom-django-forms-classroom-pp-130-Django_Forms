from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'count', 'get_authors')  # виводимо id, назву, кількість і авторів
    search_fields = ('name', 'authors__surname', 'authors__name')  # пошук по назві книги та по іменах авторів
    list_filter = ('count',)  # можна фільтрувати за кількістю (або інші логічні поля)

    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'description', 'count', 'authors')
        }),
    )

    def get_authors(self, obj):
        return ", ".join([f"{author.surname} {author.name}" for author in obj.authors.all()])
    get_authors.short_description = 'Authors'  # заголовок колонки в адмінці
