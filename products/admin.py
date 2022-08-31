from django.contrib import admin
from . models import Book, Fiction, NonFiction, Child, Urdu, Horror


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'stock',)
class FictionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'stock',)
class NonFictionAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'stock',)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'stock',)
class UrduAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'stock',)
class HorrorAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_name', 'price', 'stock',)

admin.site.register(Book, BookAdmin)
admin.site.register(Fiction, FictionAdmin)
admin.site.register(NonFiction, NonFictionAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Urdu, UrduAdmin)
admin.site.register(Horror, HorrorAdmin)
