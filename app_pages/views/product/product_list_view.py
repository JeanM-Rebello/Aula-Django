from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from app_pages.models import ProductModel

class ProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ProductModel
    template_name = 'products/list_products.html'
    context_object_name = 'object_list'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        return redirect('pages:home')
