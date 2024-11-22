from django.urls import path
from .views import index, job_details

urlpatterns = [
    path('',index ,name='home'),
    path('<int:pk>/details',job_details ,name='details'),
]
