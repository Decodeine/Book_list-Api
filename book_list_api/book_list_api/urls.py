from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book_app.urls')),  # Include the URL patterns from the 'book_app' app
]
