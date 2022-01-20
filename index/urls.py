from index.views import MyTokenObtainPairView, UserRegister, VerifyUser
from django.urls import path, include

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegister.as_view(), name='register_user'),
    path('verify_user/', VerifyUser.as_view(), name='verify_user')
]