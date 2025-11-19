from django.shortcuts import render ,redirect
from django.contrib.auth import login  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from django.views.generic.detail import DetailView
from .models import Book, Library 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required 
from .models import Library
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# ------------------------------
# Function-based view
# ------------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ------------------------------
# Class-based view
# ------------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library'  

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm()  
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()  
    return render(request, 'relationship_app/register.html', {'form': form})  
def check_role(role):
    def decorator(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == role
    return decorator


@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})