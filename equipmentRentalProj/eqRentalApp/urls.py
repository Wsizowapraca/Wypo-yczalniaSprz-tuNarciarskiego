from django.urls import path

from . import views


urlpatterns = [
    path('equipment/', views.equipment_view, name='equipment'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    # path('change_password/', views.change_password_view, name='change-password'),
    path('rent/<str:pk>', views.rent_view, name='rent'),
    path('your_rents/', views.your_rents_view, name='your-rents')
    # path('create_new_rent/', views.create_new_rent, name='create-new-rent')
]
