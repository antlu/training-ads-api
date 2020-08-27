from django.urls import path

from ads.views import AdDetails, AdList

urlpatterns = [
    path('', AdList.as_view()),
    path('<int:pk>', AdDetails.as_view()),
]
