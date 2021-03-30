from django.urls import path
from . import views

urlpatterns =[
	path('', views.home, name='home'),
	path('add_items', views.add_items, name='add_items'),
	path('category', views.add_category, name='category'),
	path('updateitems/<int:pk>/', views.update_items, name='updateitems'),
	path('stockdetail/<int:pk>/', views.stock_detail, name='stockdetail'),
	path('issueitems/<int:pk>/', views.issue_items, name='issueitems'),
	path('receiveitems/<int:pk>/', views.receive_items, name='receiveitems'),
	path('reorderlevel/<int:pk>/', views.reorder_level, name='reorderlevel'),
	path('list_item/', views.list_item, name='list_item'),
	path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
]