from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('book', views.book),
    path('author', views.author),
    path('auth', views.auth),
    path('authinfo/<authorid>', views.authInfo),
    path('bookinfo/<bookid>', views.bookInfo),
    path('authUpdate/<bookid>', views.authUpdate),
]