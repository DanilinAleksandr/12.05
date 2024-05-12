from django.urls import path
from .views import index, week, month, year
from .views import upload_image

urlpatterns = [
    path('', index, name='index'),
    path('week/<int:client_id>', week, name='week'),
    path('month/<int:client_id>', month, name='month'),
    path('year/<int:client_id>', year, name='year'),
    path('upload/<int:product_id>', upload_image, name='upload_image'),
]
