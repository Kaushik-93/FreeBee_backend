from django.urls import path

from . import views

urlpatterns = [ 
    path('donor_api/', views.DonorAPI.as_view()),
    path('orphanage_api/', views.OrphanageAPI.as_view()),
]