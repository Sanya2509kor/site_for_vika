from django.shortcuts import render
from django.views.generic import CreateView


class BookingView(CreateView):
    template_name = 'booking/booking.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запись'
        context['title_text'] = 'Выбирите дату и время посещения'
        # context['text'] = 'Выберите стиль, который подчеркнет вашу индивидуальность'
        # context['goods'] = Products.objects.all()
        return context
    

    def get_queryset(self):
        pass
        # goods = Products.objects.all()
        # return goods
    

