from django.contrib import admin
from django.urls import path, include

import accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('account/',include('django.contrib.auth.urls')),
    path('account/', include('accounts.urls')),
]
