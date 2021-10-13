from django.contrib import admin

from django.contrib import admin
from .models import Project, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "description",)


admin.site.register(Project, ProjectAdmin)
