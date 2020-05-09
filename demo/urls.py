import os
from django.contrib import admin
from django.views.static import serve
from django.conf.urls import include, url
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

doc_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs/')

def docs(request):
    from django import http
    return http.HttpResponsePermanentRedirect(os.path.join(request.path, 'index.html'))


swingtime_patterns = [
    path('', TemplateView.as_view(template_name='intro.html'), name='demo-home'),
    path('karate/', include('karate.urls')),
    path('admin/', admin.site.urls),
    path('docs/', docs, name='swingtime-docs'),
    path('docs/(<path>.*)', serve, dict(document_root=doc_root, show_indexes=False))
]

urlpatterns = [
    path('', RedirectView.as_view(url='/swingtime/')),
    path('swingtime/', include(swingtime_patterns)),
]
