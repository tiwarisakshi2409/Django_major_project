from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('seller-index/',views.seller_index,name='seller-index'),
    path('product/<str:cat>/',views.product,name='product'),
    path('shoping-cart/',views.shoping_cart,name='shoping-cart'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('change-password/',views.change_password,name='change-password'),
    path('profile/',views.profile,name='profile'),
    path('seller-add-product/',views.seller_add_product,name='seller-add-product'),
    path('seller-view-product/',views.seller_view_product,name='seller-view-product'),
    path('seller-product-details/<int:pk>/',views.seller_product_details,name='seller-product-details'),
    path('seller-product-edit/<int:pk>/',views.seller_product_edit,name='seller-product-edit'),
    path('seller-product-delete/<int:pk>/',views.seller_product_delete,name='seller-product-delete'),
    path('product-details/<int:pk>/',views.product_details,name='product-details'),
    
]