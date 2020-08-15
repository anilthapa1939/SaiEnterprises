from django.urls import path
from . import views
urlpatterns =[
    path('',views.Home,name='home'),
    path('aboutus',views.Aboutus,name='aboutus'),
    path('contactus',views.Contactus,name='contactus'),
    path('gallery',views.Gallery,name='gallery'),
     path('sg',views.Sg,name=''),
    path('bouncers',views.Bouncers,name='bouncers'),
    path('hs',views.Hs,name='hs'),
    path('sss',views.Sss,name='sss'),
    path('hsk',views.Hsk,name='hsk'),
    path('ms',views.Ms,name='ms'),
    path('ob',views.Ob,name='ob'),
    path('gs',views.Gs,name='gs'),
]