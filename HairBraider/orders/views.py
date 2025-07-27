from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import AppointmentForm
from .models import AvailableDate, AvailableTime, Appointment
from django.views.generic import CreateView
from django.db import transaction
from django.contrib import messages


class AppointmentView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'orders/appointment.html'
    success_url = reverse_lazy('main:index')


    def form_valid(self, form):
        try:
            with transaction.atomic():
                # Получаем выбранный временной слот
                time_slot = form.cleaned_data['time']
                
                # Блокируем запись на время транзакции
                locked_time_slot = AvailableTime.objects.select_for_update().get(pk=time_slot.pk)
                
                # Проверяем доступность
                if not locked_time_slot.freely:
                    form.add_error('time', 'Это время уже занято')
                    return self.form_invalid(form)
                
                # Сохраняем запись
                self.object = form.save(commit=False)
                self.object.time = locked_time_slot
                self.object.save()
                
                # Обновляем статус времени
                locked_time_slot.freely = False
                locked_time_slot.save()
                
                messages.success(self.request, 'Запись успешно создана!')
                return super().form_valid(form)
                
        except AvailableTime.DoesNotExist:
            form.add_error('time', 'Выбранное время не найдено')
            return self.form_invalid(form)
        except Exception as e:
            form.add_error(None, f'Произошла ошибка: {str(e)}')
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Пожалуйста, исправьте ошибки в форме')
        return super().form_invalid(form)
    

# def appointment_view(request):
#     form = AppointmentForm(request.POST or None)
    
#     if request.method == 'POST' and form.is_valid():
#         try:
#             # 1. Сохраняем запись о бронировании (пока без коммита)
#             appointment = form.save(commit=False)
            
#             # 2. Получаем выбранные дату и время
#             selected_date = form.cleaned_data['date']
#             selected_time_obj = form.cleaned_data['time']  # Это объект AvailableTime
            
#             # 3. Проверяем доступность времени
#             if not selected_time_obj.freely:
#                 form.add_error('time', 'Это время уже занято')
#             else:
#                 # 4. Обновляем статус времени
#                 selected_time_obj.freely = False
#                 selected_time_obj.save()
                
#                 # 5. Связываем время с записью
#                 appointment.time = selected_time_obj
#                 appointment.save()
                
#                 return redirect('main:index')
                
#         except Exception as e:
#             form.add_error(None, f'Произошла ошибка: {str(e)}')
    
#     return render(request, 'orders/appointment.html', {'form': form})



def load_times(request):
    date_id = request.GET.get('date')
    times = AvailableTime.objects.filter(date_id=date_id, freely=True)
    return render(request, 'orders/times_dropdown_list_options.html', {'times': times})

# def success_view(request):
#     return render(request, 'orders/success.html')