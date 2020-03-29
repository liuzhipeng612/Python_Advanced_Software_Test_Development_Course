from rest_framework.pagination import PageNumberPagination


class ManualPageNumberPagination(PageNumberPagination):
    # 当前用户指定的页面key的名称
    page_query_param = 'p'
    # 当前用户指定的每一页条数key的名称
    page_size_query_param = 's'
    # 前端能指定的每一页最多数据条数（当前不超过100条）
    max_page_size = 100
    # 指定默认每一页2条数据
    page_size = 2
