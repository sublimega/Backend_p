from django.urls import path
from .views import HompageView, AboutView




urlpatterns = [
    path('', HompageView.as_view(), name='homeview'),
    # path('submit_user/', Submit.as_view(), name='submit-user'),
    path('about/', AboutView.as_view(), name='about'),
    
   

]