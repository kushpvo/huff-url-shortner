from django.urls import path
from .views import RedirectToLongURLView, LinkCreateView, LinkDetailView
from . import views

urlpatterns = [
    path('<str:short_url_code>/', RedirectToLongURLView.as_view(),
         name='redirect_to_long_url'),
    path('', LinkCreateView.as_view(), name='link_create'),
    path('link/<int:pk>/',
         LinkDetailView.as_view(), name="link_detail")
]
