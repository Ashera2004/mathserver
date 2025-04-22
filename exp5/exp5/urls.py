from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('power/', views.calc_power, name='power'),  # Path for the power view
    path('', views.calc_power, name='power_root'),  # Root path to point to calc_power view
]
