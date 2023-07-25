from django.urls import path
from .views import InfoRequestList, InfoRequestDetail, InfoRequestCreate, SuccessView

urlpatterns = [
    path('', InfoRequestList.as_view(), name='info_request_list'),
    path('<int:pk>', InfoRequestDetail.as_view(), name='info_request_detail'),
    path('info/', InfoRequestCreate.as_view(), name='info_request_create'),
    path('info/success/', SuccessView.as_view(), name='success_page'),
]
