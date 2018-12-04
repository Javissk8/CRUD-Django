from django.contrib import admin
from .models import UserProfile, Category, Business, Promo, CommentBusiness


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number','birthday')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name','hours','email','address','last_modified','created_at')

class PromoAdmin(admin.ModelAdmin):
    list_display = ('name','description','business')

class CommentBusinessAdmin(admin.ModelAdmin):
    list_display = ('comment','created_at','score','user','business')


# Register your models here.

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(CommentBusiness, CommentBusinessAdmin)