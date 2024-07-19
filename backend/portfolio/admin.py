from django.contrib import admin
from .models import Course, Experience, Project, Resume, Skill, Stack


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin View for Project)"""

    list_display = (
        "title",
        "slug",
    )


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """Admin View for Resume)"""

    list_display = (
        "name",
        "surname",
        "position",
        "github_url",
    )


@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    """Admin View for Stack)"""

    list_display = ("title", "slug", 'queue')
    list_editable = ('queue',)
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin View for Course)"""

    list_display = (
        "title",
        "company",
        "date_start",
        "date_end",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin View for Skill)"""

    list_display = ("title",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Admin View for Experience)"""

    list_display = (
        "vacancy_title",
        "company",
        "date_start",
        "date_end",
    )
