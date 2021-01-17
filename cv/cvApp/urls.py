from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('news/<int:pk>/', ViewWork.as_view(), name='view_work')
]
