from django.urls import path
from . import views

urlpatterns = [
    path('dec-to-bin/', views.dec_to_bin, name='dec_to_bin_form'),
    path('dec-to-bin/<int:number>/', views.dec_to_bin, name='dec_to_bin'),
    path('hex-to-dec/', views.hex_to_dec, name='hex_to_dec'),
    path('hex-to-dec/form/', views.hex_to_dec, name='hex_to_dec_form'),
]
