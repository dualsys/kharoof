from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from customerapi import views
from newtestapp.views import PurchaseListViewSet,FeedViewSet
from rest_framework.urlpatterns import format_suffix_patterns
router = routers.DefaultRouter()
router.register(r'Products',views.ProductsViewset)
router.register(r'Customers',views.CustomersViewset)
router.register(r'Order',views.OrderViewset)
router.register(r'OrderTimeLine',views.OrderTimeLineViewset , basename='OrderTimeLine')
#router.register(r'LoginToApp',views.LoginToApp)

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

#router.register(r'OrderTimeLine(?P<order_id>.+)/$',views.OrderTimeLineViewset.as_view(), basename='models.OrderTimeLine')
urlpatterns = [
    url('admin/', admin.site.urls),
    #path('',include(views.home, name="home"))
    url('api/v1/', include(router.urls)),
    #path('api/auth/', include('djoser.urls.authtoken')),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
]
