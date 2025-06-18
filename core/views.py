from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import * 
from django.contrib import messages
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import DestinationSerializer
from .forms import DestinationForm
import requests
# Create your views here.

class ListDestinationView(ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    
class CreateDestinationView(CreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetailView(RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    
class DestinationUpdateView(UpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = 'pk'
    parser_classes = [MultiPartParser, FormParser]

class DeleteDestinationView(DestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    lookup_field = 'pk'

    
def index(request):
    list(messages.get_messages(request))
    api_url = 'http://127.0.0.1:8000/api/list'
    data = None
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
        else:
            messages.error(request, 'Some error occurred')
    except requests.RequestException as e:
        messages.error(request, 'Request exception')
    if data:
        return render(request, 'index.html', {'data': data})
    else:
        return render(request, 'index.html')
    

def create_destination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')
        if not images:
            messages.error(request, 'At least one image is required')
            
        elif form.is_valid():
            data = form.cleaned_data
            
            files = []
            for i, image in enumerate(images):
                files.append(('images', (image.name, image.file, 'image/jpeg')))
            api_url = f'http://127.0.0.1:8000/api/create'
            try:
                response = requests.post(api_url, data=data, files=files)
                print(f"API status: {response.status_code}")
                print(f'API response: {response.text}')
                if response.status_code in (200, 201):
                    messages.success(request, 'Destination created successfully')
                    return redirect(reverse('index'))
                else:
                    messages.error(request, f'API error: {response.status_code}')
            except requests.RequestException:
                messages.error(request, 'Failed to connect to API')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = DestinationForm()
    return render(request, 'create_destination.html', {'form': form})

           
def view_destination(request, pk):
    api_url = f"http://127.0.0.1:8000/api/{pk}"
    data = None
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
        elif response.status_code == 404:
            messages.error(request, 'Destination not found')
        else:
            messages.error(request, 'Some error occured')
    except requests.RequestException:
        messages.error(request, 'Request exception')        
    if data:
        print(data)
        images = Image.objects.filter(destination__name=data['name'])
        context = {'destination': data, 'images': images}
        return render(request, 'view_destination.html', context)
    else:
        return redirect('index')

        
 
            
def update_destination(request, pk):
    destination = get_object_or_404(Destination, id=pk)
    list(messages.get_messages(request))

    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        images = request.FILES.getlist('images')
        if form.is_valid():
            data = form.cleaned_data
            files = [('images', img) for img in images]
            api_url = f"http://127.0.0.1:8000/api/{pk}/update"
            try:
                response = requests.put(api_url, data=data, files=files)
                if response.status_code in (200, 204):
                    messages.success(request, 'Destination updated successfully')
                    return redirect('index')
                else:
                    print(f'API response status code: {response.status_code}')
                    messages.error(request, 'API error')
            except requests.RequestException:
                messages.error(request, 'Failed to connect to API')
        else:
            messages.error(request, 'Invalid form data')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'update_destination.html', {'form': form, 'destination': destination})


def delete_destination(request, pk):
    api_url = f'http://127.0.0.1:8000/api/{pk}/delete'
    if request.method == 'POST':
        try:
            response = requests.delete(api_url)
            if response.status_code == 204:
                messages.success(request, 'Destination deleted')
                return redirect('index')
            else:
                messages.error(request, 'Failed to delete destination')
                return redirect('index')

        except requests.RequestException:
            messages.error(request, 'Error connecting to deletion API')
    return redirect('index')
    