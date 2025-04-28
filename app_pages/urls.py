from django.urls import path
from app_pages.views import(
    HomeView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name='pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('listar/', ProductListView.as_view(), name='list_product'),
    path('criar/', ProductCreateView.as_view(), name='create_product'),
    path('editar/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('deletar/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]