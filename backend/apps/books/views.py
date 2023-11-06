from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


class BookListView(ListView):
    '''посмотреть и почитать документацию'''
    model = Book
    template_name = 'book_list.html'

