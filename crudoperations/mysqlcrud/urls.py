from django.urls import path
from mysqlcrud import views


urlpatterns = [
    path('create',views.createempview),
    # path('userreg/',views.userreg),
    # path('insertuser/',views.insertuser),

]
