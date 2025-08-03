from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm
from orders.models import Appointment
from django.utils import timezone


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context
    
    def get_success_url(self):
        redirect_page = self.request.POST.get('next', None)
        if redirect_page and redirect_page != reverse('user:logout'):
            return redirect_page
        return reverse_lazy('main:index')
    
    def form_valid(self, form):
        # session_key = self.request.session.session_key
        user = form.get_user()

        if user:
            auth.login(self.request, user)
            # if session_key:
                # forgot_carts = Cart.objects.filter(user=user)
                # if forgot_carts.exists():
                    # forgot_carts.delete()
                # Cart.objects.filter(session_key=session_key).update(user=user)
            messages.success(self.request, f"{user.username}, Вы вошли в аккаунт!")

            return HttpResponseRedirect(self.get_success_url())
        

    def form_invalid(self, form):
        messages.error(self.request, "Неверный номер телефона или пароль")
        return super().form_invalid(form)    
    
        
    



class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:profile')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context
    
    def form_valid(self, form):
        # session_key = self.request.session.session_key
        user = form.instance
        
        if user:
            form.save()
            auth.login(self.request, user)

        # if  session_key:
            # Cart.objects.filter(session_key=session_key).update(user=user)
            
        messages.success(self.request, f"{user.username}, Вы успешно зарегистрированы и вошли в аккаунт")
        return HttpResponseRedirect(self.success_url)
    



class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, "Данные успешно обновлены")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Произошла ошибка')
        return super().form_invalid(form)    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личный кабинет'
        if self.request.user.is_authenticated:
            user_app = Appointment.objects.filter(user=self.request.user)
            today = timezone.now().date()
            context['current_app'] = user_app.filter(date__date=today)
            context['past_app'] = user_app.filter(date__date__lt=today)
            context['future_app'] = user_app.filter(date__date__gt=today)

        # context['orders'] = Order.objects.filter(user=self.request.user).prefetch_related(
                # Prefetch(
                    # "orderitem_set",
                    # queryset=OrderItem.objects.select_related("product"),
                # )
            # ).order_by("-id")
        return context



# class UserCartView(TemplateView):
#     template_name = 'users/users_cart.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Корзина'
#         return context

# def users_cart(request):
#     return render(request, 'users/users_cart.html')



@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))
