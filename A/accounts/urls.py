from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls

# {
#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MTg3NDczOCwiaWF0IjoxNjcxNzg4MzM4LCJqdGkiOiI3YTdjNjQwMTFmZDg0Nzg5OTIxMzgxMzI4MjEyNTMwNyIsInVzZXJfaWQiOjF9.pNlMhNvzQ3rwxY4er0QK235Xocw1SlOc8F19OmOgpL0",
#     "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxNzg4NjM4LCJpYXQiOjE2NzE3ODgzMzgsImp0aSI6Ijc0MDVhNDZmZTA5NjRmZjU5MWEwOTRlMTYwMzE0NTczIiwidXNlcl9pZCI6MX0.6snafkDx-b1fR1l0LV1iftIP88hUdeHBK1iNuu_7eqE"
# }