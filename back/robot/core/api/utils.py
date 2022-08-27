from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultSetPagination(PageNumberPagination):
    page_size = 25
    max_page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'size'
    last_page_strings = 'last'
    template = None

    def get_paginated_response(self, data):
        return Response({'total': self.page.paginator.count, 'result': data})
