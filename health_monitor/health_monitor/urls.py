"""
URL configuration for health_monitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, re_path, include  
from graphene_django.views import GraphQLView
#from sleep_tracker.views import home
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
import logging
from django.shortcuts import redirect
from graphql import GraphQLError
from sleep_tracker import views 

logger = logging.getLogger(__name__)

class CustomGraphQLView(GraphQLView):
    def execute_graphql_request(self, *args, **kwargs):
        # Log the incoming request's body for debugging
        logger.info(f"GraphQL request body: {self.request.body}")
        return super().execute_graphql_request(*args, **kwargs)
    def format_error(self, error):
        if isinstance(error, GraphQLError):
            return {'message': str(error), 'locations': error.locations, 'path': error.path}
        return super().format_error(error)

@require_http_methods(["GET", "POST", "OPTIONS"])
def graphql_view(request):
    if request.method == 'OPTIONS':
        return HttpResponse(status=204)
    return GraphQLView.as_view()(request)

def render_react(request):
    return render(request, "index.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", csrf_exempt(CustomGraphQLView.as_view(graphiql=True))),
    path('', render_react),
    re_path(r'^graphql//$', lambda request: redirect('/', permanent=True)),
    #re_path(r"^(?:.*)/?$", render_react),
    #path('api/', include('health_monitor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)