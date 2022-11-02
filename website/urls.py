from django.urls import path
from .views import IndexView, PortfolioView

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]
