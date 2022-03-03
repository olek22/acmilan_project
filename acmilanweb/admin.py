from django.contrib import admin
from .models import Club, Profile


# Register your models here.
#admin.site.register(Club)
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    #fields = ["name"]
    exclude = ["description"]
    list_display = ["name", "stadium_with_capacity"]
    list_filter = ["name"]
    search_fields = ["stadium"]

admin.site.register(Profile)