from django.contrib import admin

from catalog.models import Product, Category, Contacts, Feedback, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'owner', 'is_published')
    list_filter = ('category', 'owner', 'is_published')
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_active')
    list_filter = ('version_number', 'version_name',)
    search_fields = ('version_name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'phone', 'message', 'created_at')



