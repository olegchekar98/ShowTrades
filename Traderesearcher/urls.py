from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^get_last_trades', views.show_trade, name='show_trade')
]
