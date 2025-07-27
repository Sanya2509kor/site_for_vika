from django import forms
from .models import AvailableDate, AvailableTime, Appointment
from django.db.models import Exists, OuterRef


class AppointmentForm(forms.ModelForm):
    date = forms.ModelChoiceField(
        queryset=AvailableDate.objects.annotate(
            has_available_times=Exists(
                AvailableTime.objects.filter(
                    date=OuterRef('pk'),
                    freely=True
                )
            )
        ).filter(has_available_times=True),
        empty_label="---------",
        to_field_name="id"  # Убедитесь, что используется правильное поле
    )
    
    class Meta:
        model = Appointment
        fields = ['date', 'time', 'name', 'phone', 'product']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].queryset = AvailableTime.objects.none()
        
        if 'date' in self.data:
            try:
                date_id = int(self.data.get('date'))
                self.fields['time'].queryset = AvailableTime.objects.filter(date_id=date_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['time'].queryset = self.instance.date.available_times.all()