from django.urls import path
from .import views
from .views import Destinationcreateview, Destinationdetailview, Destinationupdateview, DestinationDeleteeview, \
    DestinationSearchview

urlpatterns = [
    path('create/',Destinationcreateview.as_view(),name='create'),
    path('detail/<int:pk>/', Destinationdetailview.as_view(), name='detail'),
    path('update/<int:pk>/', Destinationupdateview.as_view(), name='update'),
    path('delete/<int:pk>/', DestinationDeleteeview.as_view(), name='delete'),
    path('search/<str:Name>/', DestinationSearchview.as_view(), name="search"),

    path('', views.place_list, name='place_list'),
    path('add/', views.add_place, name='add_place'),
    path('update/<int:pk>/', views.update_place, name='update_place'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('detail/<int:pk>/',views.place_detail,name ='detail')

]
