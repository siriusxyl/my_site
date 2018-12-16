# -*- coding:utf-8 -*-
import httplib
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse


def json_http_success(result=None):
    """
    统一接口正常返回格式
    接口正常时的返回json数据，会额外添加{error_code:0, error_msg: ''}
    """
    return json_http_response_extend(result)


def json_http_error(error_msg, error_code=1, result=None, status=httplib.BAD_REQUEST):
    """
    统一接口错误返回格式
    :param error_msg: 错误消息
    :param error_code: 错误代码，默认为1
    :param result: 附带的错误数据，一般不需要用
    :param status: 状态码，默认为400
    :return:
    """
    return json_http_response_extend(result, error_code, error_msg, status)


def json_http_response_extend(result=None, error_code=0, error_msg=u'', status=httplib.OK):
    response = {"error_code": error_code, "error_msg": error_msg}
    if result:
        response.update(result)
    return json_http_response(response, status=status)


def json_http_response(result, status=httplib.OK, cls=DjangoJSONEncoder):
    return HttpResponse(content=json.dumps(result, cls=cls, ensure_ascii=True, encoding="utf-8"),
                        content_type="application/json; charset=UTF-8", status=status)


def string_http_response(result, status=httplib.OK):
    return HttpResponse(content=result,
                        content_type="application/json; charset=UTF-8", status=status)