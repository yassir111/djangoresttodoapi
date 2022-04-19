from rest_framework import pagination

class CustomPagePagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'count'
    max_page_size = 3
    page_query_param = 'p'