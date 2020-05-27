from rest_framework import pagination

class Pagination(pagination.PageNumberPagination):
    #how many show in each
    page_size = 15
    #name of page count, like page=3
    page_query_param = 'page'
    #change how many will show in each page
    page_size_query_param = 'many'
    #max of set in many, but I will let just 15 like first one
    max_page_size = 15