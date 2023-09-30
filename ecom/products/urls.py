# from .views import *

from .views import *
from django.urls import path

urlpatterns = [
     path('products', ProductView.as_view()),
     path('demo',DemoView.as_view)
]     
