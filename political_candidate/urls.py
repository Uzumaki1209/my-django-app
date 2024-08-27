# Import the necessary modules from Django
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Define the URL patterns for the project
urlpatterns = [
    # Admin URL - maps to Django's built-in admin interface, accessible at /admin/
    path('admin/', admin.site.urls),
    
    # Root URL - redirects to the 'webapp/' URL
    path('', lambda request: HttpResponseRedirect('webapp/')),
    
    # Webapp URL - includes all URL patterns defined in the 'campaign' app's urls.py file, accessible at /webapp/
    path('webapp/', include('campaign.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)