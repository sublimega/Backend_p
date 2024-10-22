from django.urls import path
from .views import HompageView, AboutView




urlpatterns = [
    path('', HompageView.as_view(), name='homeview'),
    path('AboutView/', AboutView.as_view(), name='about'),
 

    
   

]