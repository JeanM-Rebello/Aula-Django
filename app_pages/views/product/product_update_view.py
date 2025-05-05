from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from app_pages.models import ProductModel
from app_pages.forms import ProductForm

class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = ProductModel
    form_class = ProductForm
    template_name = 'products/update_product.html'
    success_url = reverse_lazy('pages:list_product')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('pages:home')