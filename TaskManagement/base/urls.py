from django.urls import path
from . import views as this_is_base_app

urlpatterns = [
    path('',this_is_base_app.home,name='home'),
    path('read/',this_is_base_app.read,name='read'),
    path('update/<int:pk>',this_is_base_app.update,name='update'),
    path('delete/<int:pk>',this_is_base_app.delete,name='delete'),
]
