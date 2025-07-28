from django.contrib import admin
from .models import AvailableDate, AvailableTime, Appointment


class AvailableTimeInline(admin.TabularInline):
    model = AvailableTime
    extra = 1


@admin.register(AvailableDate)
class AvailableDateAdmin(admin.ModelAdmin):
    inlines = [AvailableTimeInline]
    list_display = ('date',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'name', 'phone', 'created_at')
    list_filter = ('date',)
    fields = [
        'user',
        'name',
        'phone',
        'date',
        'time',
        'comment',
        'product',     
    ]

    def date_str(self):
        return self.date