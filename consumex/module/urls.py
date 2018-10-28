from django.urls import re_path
from .views import HomeView, ContactView, AboutView, PortFolioView, ServicesView

urlpatterns = [
    re_path('^$', HomeView.as_view(), name='home'),
    re_path('^contact-us$', ContactView.as_view(), name='contact-us'),
    re_path('^about$', AboutView.as_view(), name='about'),
    re_path('^portfolio$', PortFolioView.as_view(), name='portfolio'),
    re_path('^services/$', ServicesView.as_view(), name='services'),
]
