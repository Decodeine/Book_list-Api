from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse,HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'author', 'publication_date']

    def get(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        return render(request, 'home.html', {'books': self.object_list})

    def post(self, request, *args, **kwargs):
        if not request.user.is_staff:  # Check if the user is an admin
            return HttpResponseForbidden("You are not allowed to create books.")
        response = super().post(request, *args, **kwargs)
        return JsonResponse(response.data)




class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return render(request, 'single_book.html', {'book': self.object})

    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        return JsonResponse(response.data)

    def patch(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        return JsonResponse(response.data)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return JsonResponse(response.data)



class ReviewListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book__id=book_id)