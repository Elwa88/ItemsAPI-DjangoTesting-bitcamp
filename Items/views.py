from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer

class PublicItemListCreate(generics.ListCreateAPIView):
    queryset = Item.objects.filter(private_item= False)
    serializer_class = ItemSerializer

class PrivateItemList(generics.ListAPIView):
    queryset = Item.objects.filter(private_item= True)
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]