from django.urls import path
from .views import index, form, regist, log_in,new_page, add_product, logout_user, myProfile


urlpatterns = [
    path('', index.as_view(), name='home'),
    path('form/', form.as_view(), name='form-page'),
    path('myProfile/', myProfile.as_view(), name='profile-page'),
    path('login/', regist.as_view(), name='regist-page'),
    path('logout/', logout_user, name="logout"),
    path('registrasi/', log_in, name='login-page'),
    path('new_page/', new_page.as_view(), name='new-page'),
    path('new_product/', add_product.as_view(), name='add-product'),
]
