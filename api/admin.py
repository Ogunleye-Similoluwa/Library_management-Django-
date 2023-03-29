from django.contrib import admin
from book.models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(LibraryUser)
class User(UserAdmin):
    pass


admin.site.register(Author)
admin.site.register(BookInstance)
