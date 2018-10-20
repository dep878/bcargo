from django.urls import path, re_path
from . import views
from .views import RecipeModelList, RecipeModelListJson

urlpatterns = [
    path('company', views.CompanyList.as_view(), name='company-list'),
    path('', RecipeModelList.as_view(), name="testmodel"),
    # path('company/add/', views.RecipeCreateView.as_view(), name='company-add'),
    path('company/add/', views.RecipeCreateView.as_view(), name='company-add'),
    path('testmodel', RecipeModelList.as_view(), name="testmodel"),
    path('testmodel_data/', RecipeModelListJson.as_view(), name="testmodel_list_json"),
    # re_path(r'company/(?P<pk>[0-9]+)/$', views.CompanyUpdate.as_view(), name='company-update'),
    # re_path(r'company/(?P<pk>[0-9]+)/delete/$', views.CompanyDelete.as_view(), name='company-delete'),
]
