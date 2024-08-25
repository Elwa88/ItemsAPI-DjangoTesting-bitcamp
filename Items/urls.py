from django.urls import path
from .views import PublicItemListCreate, PrivateItemList

urlpatterns = [
    path('items/',PublicItemListCreate.as_view()),
    path('private_items/',PrivateItemList.as_view())
]
