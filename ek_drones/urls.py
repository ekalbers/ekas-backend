from django.urls import path
from .views import InfoRequestList, InfoRequestDetail, InfoRequestCreate

urlpatterns = [
    path('', InfoRequestList.as_view(), name='info_request_list'),
    path('<int:pk>', InfoRequestDetail.as_view(), name='info_request_detail'),
    path('info/', InfoRequestCreate.as_view(), name='info_request_create'),
]
