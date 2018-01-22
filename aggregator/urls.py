"""aggregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from newsfeed.views import PostList, PostDetail, SourceList, SourcePostList

urlpatterns = [
    url(r'^$', PostList.as_view(), name="posts"),
    url(r'^admin/', admin.site.urls),
    url(r'^source/(?P<source_id>\d+)/$', SourcePostList.as_view(), name="posts_by_source"),
    url(r'^sources/', SourceList.as_view(), name="sources"),
    url(r'^(?P<slug>[-\w]+)/$', PostDetail.as_view(), name="post-detail"),
    url('', include('pwa.urls')),  # You MUST use an empty string as the URL prefix
]


if 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]


