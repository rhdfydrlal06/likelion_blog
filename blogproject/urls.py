from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings #media쓰기 위해 필요
from django.conf.urls.static import static #외우기 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home,name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio/',portfolio.views.portfolio,name='portfolio'),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

