from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Training,Job

@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'duration', 'location')
    search_fields = ('title', 'provider', 'location')
    list_filter = ('provider', 'location', 'duration')
    ordering = ('title',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'pay_rate', 'posted_on')
    search_fields = ('title', 'employer__username', 'location')
    list_filter = ('location',)
    ordering = ('-posted_on',)