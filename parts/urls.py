from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('orders_list.html', views.orders_list, name='orders_list'),
    path('order_from_file.html', views.order_from_file, name='order_from_file'),
    path('order_new.html', views.order_new, name='order_new'),
    path('cart/', include('cart.urls')),
    path('create/', views.order_create, name='order_create'),
    path('product/', views.product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
