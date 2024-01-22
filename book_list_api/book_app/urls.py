from django.urls import path
from . import views
from .views import ReviewListView #book_list_view

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.SingleBookView.as_view()),
    path('books/<int:book_id>/reviews/', ReviewListView.as_view(), name='book_reviews'),
    #path('books/', book_list_view, name='books'),
]