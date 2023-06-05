from django.urls import path
from . import views
app_name = 'fabric'

urlpatterns = [
    path('<int:pk>', views.LoanDetailsView.as_view(), name='loan-details'),
]
