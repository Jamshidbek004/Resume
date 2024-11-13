# resume_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('malumot/', views.malumot, name='malumot'),
    path('', views.asosiy, name='asosiy'),
    path('qr/', views.generate_qr_code, name='generate_qr_code'),
    path('add_website/', views.add_website, name='add_website'),
    path('add_resume/', views.add_resume, name='add_resume'),
    path('add_tajriba/', views.add_tajriba, name='add_tajriba'),
    path('add_malaka', views.add_malaka, name='add_malaka'),
    path('resume/<int:pk>/edit/', views.ResumeEditView.as_view(), name='resume_edit'),
    path('resume/<int:pk>/delete/', views.ResumeDeleteView.as_view(), name='resume_delete'),
    path('tajriba/<int:pk>/edit/', views.TajribaEditView.as_view(), name='tajriba_edit'),
    path('tajriba/<int:pk>/delete/', views.TajribaDeleteView.as_view(), name='tajriba_delete'),
    path('malaka/<int:pk>/edit/', views.MalakaEditView.as_view(), name='malaka_edit'),
    path('malaka/<int:pk>/delete/', views.MalakaDeleteView.as_view(), name='malaka_delete'),
    path('website_edit/<int:pk>/edit/', views.SaytEditView.as_view(), name='website_edit'),
    path('website_delete/<int:pk>/delete/', views.SaytDeleteView.as_view(), name='website_delete')
]
