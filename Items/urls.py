from django.urls import path
from .views import PublicItemListCreate, PrivateItemList

urlpatterns = [
    path('items/',PublicItemListCreate.as_view(),name='public'),
    path('private_items/',PrivateItemList.as_view(),name='private')
]
