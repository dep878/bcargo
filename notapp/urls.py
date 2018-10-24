from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.TestView.as_view(), name='test'),
    # path('company/add/', views.RecipeCreateView.as_view(), name='company-add'),
    # path('company/add/', views.RecipeCreateView.as_view(), name='company-add'),
    # re_path(r'company/(?P<pk>[0-9]+)/$', views.CompanyUpdate.as_view(), name='company-update'),
    # re_path(r'company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company-delete'),
]
