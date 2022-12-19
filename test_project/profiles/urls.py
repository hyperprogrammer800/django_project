from django.urls import path
from .views import profile, ProfileListView, ProfileDetailView

urlpatterns = [
    path('',ProfileListView.as_view(), name='users-home'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/', profile, name='profile'),
]
