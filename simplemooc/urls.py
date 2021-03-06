"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from simplemooc.core import urls as core_url
from simplemooc.courses import urls as courses_url
from simplemooc.accounts import urls as accounts_url
from simplemooc.forum import urls as forum_url


urlpatterns = [
	path('', include(core_url, namespace='core')),
    path('conta/', include(accounts_url, namespace='accounts')),
	path('cursos/', include(courses_url, namespace='courses')),
    path('forum/', include(forum_url, namespace='forum')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)