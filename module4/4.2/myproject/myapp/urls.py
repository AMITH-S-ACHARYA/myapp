

from django.urls import path
from myapp.views import construct_csv_from_model,construct_pdf_from_model

urlpatterns = [
    path('csv/', construct_csv_from_model),
    path('pdf/', construct_pdf_from_model),
]
