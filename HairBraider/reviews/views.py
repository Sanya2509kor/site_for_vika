from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from reviews.models import Reviews
from reviews.forms import ReviewForm


class ReviewsView(ListView):
    template_name = 'reviews/reviews.html'
    model = 'Reviews'
    context_object_name = 'reviews'
    paginate_by = 10
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        objects = Reviews.objects.all()
        return objects


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Reviews
    form_class = ReviewForm
    success_url = reverse_lazy('user:profile')
    template_name = 'reviews/make_review.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
