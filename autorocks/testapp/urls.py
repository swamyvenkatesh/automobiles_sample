from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home/', views.index, name='indexpage'),    
    url(r'^get/',views.getdatafmexcel,name='getdata'),
    url(r'^done/',views.donedata,name='donedetails'),
	url(r'^searchdet/',views.seachdetails,name='searchdat'),
    ]
    