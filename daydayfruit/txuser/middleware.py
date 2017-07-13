# coding=utf-8


# 中间件，用于记录登录前浏览的网页
class UrlPathMiddleware:
    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.get_full_path()
        if request.path not in ['/user/register/',
                                '/user/login/',
                                '/user/login_handle/',
                                '/user/register_handle/',
                                '/user/register_valid/',
                                '/user/logout/', ]:
            request.session['url_path'] = path