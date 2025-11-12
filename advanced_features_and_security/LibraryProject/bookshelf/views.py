from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # كود إنشاء كتاب جديد
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # كود تعديل كتاب
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # كود حذف كتاب
    pass
