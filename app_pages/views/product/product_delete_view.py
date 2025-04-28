from django.shortcuts import redirect
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from app_pages.models import ProductModel

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ProductModel
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('pages:list_product')
    
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('pages:home')
