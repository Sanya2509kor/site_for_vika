from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from about.models import Portfolio


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обо мне'
        return context



class PortfolioView(ListView):
    template_name = 'about/portfolio.html'
    model = 'Portfolio'
    context_object_name = 'objects'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Портфолио'
        return context
    
    def get_queryset(self):
        objects = Portfolio.objects.all()
        return objects
    


class ContactsView(TemplateView):
    template_name = 'about/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context
    
