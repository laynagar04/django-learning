from django.urls import path,include
from . import views

#template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),

]
