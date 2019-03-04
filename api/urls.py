from django.urls import path

from api.views import contacts, contact

urlpatterns = [
    path('contacts/', contacts, name='contacts'),  # GET, POST
    path('contact/<str:contact_id>/', contact, name='contact')  # GET, PUT, DELETE
]
