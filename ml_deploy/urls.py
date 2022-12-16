from django.urls import path
from . import views

app_name = 'ml_deploy'

urlpatterns = [
    # as view 메소드는 클래스형 뷰에서만 쓰는 거고
    path('', views.IrisHome.as_view(), name = 'iris_home'),
    # IRIS Predict은 fbc
    path('predict/', views.irisPredict , name = 'iris_predict'),
]