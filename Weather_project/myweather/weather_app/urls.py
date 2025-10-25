from django.urls import path , include
from . import views

urlpatterns = [
    path('predict_churn/' , views.index)
]
