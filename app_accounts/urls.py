from django.urls import path
from django.contrib.auth.views import LogoutView
from app_accounts.views import(
    LoginView,
    RegisterView,
)

app_name='accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registro/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
]