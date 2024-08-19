from django.urls import path
from .views import HomePage , AboutPage

urlpatterns = [
    path('',HomePage),
    path('about/',AboutPage)
]

