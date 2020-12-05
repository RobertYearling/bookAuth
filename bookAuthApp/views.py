from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author # This is the models.py Database

# Create your views here.

def main(request):
    context = {
        "the_books" : Book.objects.all(), #Book Class model.py
    }
    return render(request, "index.html", context)

def book(request):
    Book.objects.create(title = request.POST['b_title'], desc = request.POST['b_desc'])
    return redirect('/')

def author(request):
    context = {
        "the_auths" : Author.objects.all(), #Author Class model.py
    }
    return render(request, "author.html", context)

def auth(request):
    Author.objects.create(first_name = request.POST['a_first'], last_name = request.POST['a_last'], notes = request.POST['a_notes'])
    # newA = Author(first_name= "jlkj")
    # newA.save()
    return redirect('/author')

def authInfo(request, authorid):
    context = {
        'selectedAuthor' : Author.objects.get(id=authorid)
    }
    return render(request, "author_info.html", context)

def bookInfo(request, bookid):
    context = {
        'selectedBook' : Book.objects.get(id=bookid),
        'allAuthors' : Author.objects.all()
    }
    return render(request, "book_info.html", context)

def authUpdate(request, bookid):
    this_book = Book.objects.get(id=bookid)
    this_auth = Author.objects.get(id = request.POST['chosenAuth'])
    this_book.authors.add(this_auth)
    return redirect(f"/bookinfo/{bookid}")