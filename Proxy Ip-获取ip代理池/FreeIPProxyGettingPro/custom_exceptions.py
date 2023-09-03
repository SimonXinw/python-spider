# _*_ coding : utf-8 _*_
"""
自定义异常类
"""


class Request500Exception(Exception):
    """
    If we receive status code of 500 durning requesting, we'll get a special page(500-page).
    In this case, the spider runs successfully, but we do not get any data.
    """
    def __init__(self, obj=None):
        self.obj = obj if obj is not None else 'unknown'

    def __str__(self):
        if self.obj == 'unknow':
            return 'The request response statu code is 500!'
        else:
            return '{} | The request response statu code is 500!'.format(self.obj.__class__.__name__)


class TryWithSelfProxyLimitException(Exception):
    """
    Use yourself proxy to re-request a url, if exceed the up limit times, throws this exception
    """
    def __init__(self, obj=None):
        pass

    def __str__(self):
        return 'Attempt to use self proxy excedding limit of times!'


class ResponseTextNoneException(Exception):
    """
    标识 self.response = None 的场景
    """
    def __init__(self):
        pass

    def __str__(self):
        return 'Self.response is None!'
