from django.contrib import admin
from .models import  Employee, Type, Category
# Register your models here.

class TypeAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Type, TypeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Category, CategoryAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','names','dni','state','genero')
    list_filter = ('genero',)

admin.site.register(Employee, EmployeeAdmin)
