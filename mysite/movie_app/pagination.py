
from rest_framework.pagination import PageNumberPagination

class MovieListPagination(PageNumberPagination):
    page_size = 4

class CategoryListPagination(PageNumberPagination):
    page_size = 4

class GenreListPagination(PageNumberPagination):
    page_size = 6
