from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import AllowAny

from .models import Destination
from rest_framework import generics
from .serializers import Destinationserializer
from .serializers import Destinationserializer
from .forms import TouristForm

# Create your views here.


class Destinationcreateview(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = Destinationserializer
    permission_classes = [AllowAny]


class Destinationdetailview(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = Destinationserializer

class Destinationupdateview(generics.RetrieveUpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = Destinationserializer


class DestinationDeleteeview(generics.DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = Destinationserializer

class DestinationSearchview(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = Destinationserializer

    def get_queryset(self):
        name =self.kwargs.get('Name')
        return Destination.objects.filter(Name__icontains =name)

def place_list(request):
    places = Destination.objects.all()
    return render(request, 'list.html', {'places': places})

def place_detail(request,pk):
    place = get_object_or_404(Destination, id=pk)
    return render(request, 'detail.html', {'place': place})

def add_place(request):
    if request.method == 'POST':
        form = TouristForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = TouristForm()
    return render(request, 'add.html', {'form': form})


def update_place(request, pk):
    place = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = TouristForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = TouristForm(instance=place)
    return render(request, 'update.html', {'form': form})


def delete_book(request, pk):
    place = get_object_or_404(Destination, pk=pk)
    place.delete()
    return redirect('place_list')
