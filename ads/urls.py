from django.urls import path

from ads.views import AdDetails, AdList

urlpatterns = [
    path('', AdList.as_view(), name='ad-list'),
    path('<int:pk>', AdDetails.as_view(), name='ad-details'),
]
