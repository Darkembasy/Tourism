from django.urls import path
from . import views
from .views import TouristSpotListView, TouristSpotCreateView, TouristSpotDetailView, TouristSpotUpdateView, TouristSpotDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('faq/', views.faq, name='faq'),
    path('intramuros/', views.intramuros, name='intramuros'),
    path('chocolate_hills/', views.chocolate_hills, name='chocolate_hills'),
    path('mayon_volcano/', views.mayon_volcano, name='mayon_volcano'),
    path('elnido_palawan', views.elnido_palawan, name='elnido_palawan'),
    path('ifugao', views.ifugao, name='ifugao'),
    path('boracay', views.boracay, name='boracay'),
    path('tourist-spots/', TouristSpotListView.as_view(), name='tourist_spot_list'),
    path('tourist-spots/create/', TouristSpotCreateView.as_view(), name='tourist_spot_form'),
    path('tourist-spots/<int:pk>/', TouristSpotDetailView.as_view(), name='tourist_spot_detail'),
    path('tourist-spots/<int:pk>/update/', TouristSpotUpdateView.as_view(), name='tourist_spot_update'),
    path('tourist-spots/<int:pk>/delete/', TouristSpotDeleteView.as_view(), name='tourist_spot_confirm_delete'),
]