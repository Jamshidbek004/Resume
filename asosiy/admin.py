from django.contrib import admin
from .models import Category, Turi, Resume, Tajriba, Malaka, Website, ContactMessage

# Category modelini admin panelida sozlash
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Ko'rsatiladigan ustunlar
    search_fields = ('name',)  # Qidiruv maydoni

admin.site.register(Category, CategoryAdmin)

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'link1', 'link2')  # Ko'rsatiladigan ustunlar
    search_fields = ('name',)  # Qidiruv maydoni

admin.site.register(Website, WebsiteAdmin)

# Turi modelini admin panelida sozlash
class TuriAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Ko'rsatiladigan ustunlar
    search_fields = ('name',)  # Qidiruv maydoni

admin.site.register(Turi, TuriAdmin)

# Resume modelini admin panelida sozlash
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'kim', 'ozi_haqida')  # Ko'rsatiladigan ustunlar
    search_fields = ('ozi_haqida',)  # Qidiruv maydoni
    list_filter = ('kim',)  # Filtrlar
    list_per_page = 10  # Bir sahifada ko'rsatiladigan yozuvlar soni

admin.site.register(Resume, ResumeAdmin)

# Tajriba modelini admin panelida sozlash
class TajribaAdmin(admin.ModelAdmin):
    list_display = ('id', 'kompaniya', 'yil', 'kim')  # Ko'rsatiladigan ustunlar
    search_fields = ('kompaniya', 'kim')  # Qidiruv maydoni
    list_filter = ('kim',)  # Filtrlar
    list_per_page = 10  # Bir sahifada ko'rsatiladigan yozuvlar soni

admin.site.register(Tajriba, TajribaAdmin)

# Malaka modelini admin panelida sozlash
class MalakaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'daraja')  # Ko'rsatiladigan ustunlar
    search_fields = ('nomi__name',)  # Qidiruv maydoni (Category nomiga asoslangan)
    list_filter = ('nomi',)  # Filtrlar
    list_per_page = 10  # Bir sahifada ko'rsatiladigan yozuvlar soni

admin.site.register(Malaka, MalakaAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Make sure 'created_at' is correctly referenced

admin.site.register(ContactMessage, ContactMessageAdmin)
