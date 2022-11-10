
from . import views
from django.urls import path

urlpatterns=[
 path('',views.home,name='home'),
 path('search',views.search,name='search'),
  path('search2',views.search2,name='search2'),
 path('addpc',views.addpc,name='addpc'),
 path('addprinter',views.addprinter,name='addprinter'),
 path('upload2',views.upload2,name='upload2'),
  path('view',views.view,name='view'),
 path('edit',views.edit,name='edit'),
 path('delete',views.delete,name='delete'),
 path('search1',views.search1,name='search1'),
 path('save',views.save,name='save'),
 path('save1',views.save1,name='save1'),
 path('upload',views.upload,name='upload'),
]