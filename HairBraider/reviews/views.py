from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from reviews.models import Reviews
from reviews.forms import ReviewForm


class ReviewsView(TemplateView):
    template_name = 'reviews/reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Reviews.objects.all()

        return context


class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Reviews
    form_class = ReviewForm
    success_url = reverse_lazy('user:profile')
    template_name = 'reviews/make_review.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
