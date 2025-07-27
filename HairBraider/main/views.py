from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Products


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HairBraider'
        context['title_text'] = 'Наши услуги'
        context['text'] = 'Выберите стиль, который подчеркнет вашу индивидуальность'
        context['goods'] = Products.objects.all()
        return context
    

    def get_queryset(self):

        goods = Products.objects.all()
        return goods
    

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ReviewsView(TemplateView):
    template_name = 'main/reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    

class ProductView(DetailView):
    template_name = 'main/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    queryset = Products.objects.prefetch_related('related_products')  # Оптимизация


    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['images'] = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg)).images.all()
        # context['related_products'] = self.object.related_products.all()[:6]  # Ограничиваем до 6 товаров
        return context
