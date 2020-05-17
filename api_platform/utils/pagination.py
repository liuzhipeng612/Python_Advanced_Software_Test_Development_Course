from rest_framework.pagination import PageNumberPagination


class GlobalPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 100
    page_size = 5
    page_query_description = "第几页"
    page_size_query_description = "每页10条"

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['current_page_num'] = self.page.number
        response.data['total_page_name'] = self.page.paginator.num_pages
        return response


class ProjectPageNumberPagination(PageNumberPagination):
    # 当前用户指定的页面key的名称
    # page_query_param = 'p'
    # 当前用户指定的每一页条数key的名称
    # page_size_query_param = 'size'
    # 前端能指定的每一页最多数据条数（当前不超过100条）
    max_page_size = 100
    # 指定默认每一页2条数据
    page_size = 5
    page_query_description = "第几页"
    page_size_query_description = "每页10条"

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['current_page_num'] = self.page.number
        response.data['total_page_name'] = self.page.paginator.num_pages
        return response
