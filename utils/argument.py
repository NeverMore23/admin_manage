#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from django.http import JsonResponse

logger = logging.getLogger("django")


def get_parameter(request, name, required=False, default=None, formatter=None):
    """
    get parameter from request
    """
    if request.method == 'GET':
        value = request.GET.get(name, default)
    elif request.method == 'POST':
        value = request.POST.get(name, default)
    else:
        raise ValueError('Method %s is not supported' % request.method)
    if not value and required:
        raise KeyError('Request parameter %s is lacked' % name)
    if isinstance(value, (str, str)):
        value = value.strip()
    if value is not None and formatter is not None:
        try:
            value = formatter(value)
        except ValueError:
            value = default
    return value


def catch_exception(func):
    """
    Decorator for views that catch exceptions and return http response error with exception information.
    """
    def wrapper(*args, **kwargs):
        try:
            ret_val = func(*args, **kwargs)
            return ret_val
        except Exception as err:
            logger.exception("func name: %s, error: %s" % (func.__name__, err))
            result = {"code": -20001, "msg": str(err)}
            return JsonResponse(result)
    return wrapper


def json_response(func):
    """
    Decorator for views that catch exceptions and return http json response error with exception information.
    """
    def wrapper(*args, **kwargs):
        try:
            ret_val = func(*args, **kwargs)
            if isinstance(ret_val, dict):
                result = {"code": 0, "msg": "", "data": ret_val}
                return JsonResponse(result)
            else:
                result = {"code": -20002, "msg": u"视图函数返回值类型必须是字典"}
                return JsonResponse(result)

        except Exception as err:
            logger.exception("func name: %s, error: %s" % (func.__name__, err))
            result = {"code": -20001, "msg": str(err)}
            return JsonResponse(result)
    return wrapper


def normalize_response(func):
    """
    Decorator for views that catch exceptions and return http response error with exception information.
    """
    def wrapper(*args, **kwargs):
        try:
            ret_val = func(*args, **kwargs)
            return {"code": 0, "msg": "", "data": ret_val}
        except Exception as err:
            logger.exception("func name: %s, error: %s" % (func.__name__, err))
            result = {"code": -20002, "msg": str(err)}
            return result
    return wrapper
