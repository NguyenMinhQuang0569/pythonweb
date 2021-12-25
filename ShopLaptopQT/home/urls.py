from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='trang chu'),
    path('shop.html', views.shop, name='cua hang'),
    path('products.html', views.products, name='san pham'),
    path('contact.html', views.contact, name='lien he'),
    path('checkout.html',views.checkout, name='thu tuc thanh toan'),
    path('aboutus.html',views.aboutus, name='gioi thieu'),
    path('news.html',views.news, name='bai viet'),
    path('productcat.html/<int:id>',views.productcat, name='san pham thep danh muc'),
    path('productdetail.html/<int:id>',views.productdetail, name='chi tiet san pham'),
    path('home/addcart',views.addcart,name='mua hang'),
    path('shoppingcart.html',views.shoppingcart,name='danh sach san pham trong gio hang'),
    
]