from .views import *
from django.urls import path
from .views import *

urlpatterns = [
    path('api/list', ListDestinationView.as_view()),
    path('api/create', CreateDestinationView.as_view()),
    path('api/<int:pk>', DestinationDetailView.as_view()),
    path('api/<int:pk>/update', DestinationUpdateView.as_view()),
    path('api/<int:pk>/delete', DeleteDestinationView.as_view()),

    path('destinations/', index, name='index'),
    path('destinations/<int:pk>', view_destination, name='view-destination'),
    path('destinations/create', create_destination, name='destination-create'),
    path('destinations/<int:pk>/update', update_destination, name='destination-update'),
    path('destinations/<int:pk>/delete', delete_destination, name='destination-delete'),
    
]
