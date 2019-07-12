from django.urls import include,path,re_path
from . import views

urlpatterns = [

    path('',views.postList),
    path('Categories/',views.categoryList),
    path('Categories/Add/',views.categoryAdd),
    path('Categories/Delete/<slug:name>',views.categoryDelete),
    re_path(r'^Category/(?P<name>[\w|\W]+)/$',views.postByCategory),

    path('Post/Add/',views.postAdd),
    re_path(r'^(?P<name>[\w|\W]+)/$',views.postDetails),
    
]
