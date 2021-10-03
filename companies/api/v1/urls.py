from django.urls import path
from companies.api.v1.views import CompanyView

app_name = 'company'

urlpatterns = [
    path('', CompanyView.as_view(), name='company'),
]
