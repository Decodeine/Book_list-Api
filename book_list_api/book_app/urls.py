from django.urls import path
from . import views
from .views import ReviewListView

urlpatterns = [
    path('books', views.BookListView.as_view()),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    path('books/<int:book_id>/reviews/', ReviewListView.as_view(), name='book_reviews'),
]