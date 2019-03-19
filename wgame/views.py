# -*- coding:utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from wgame.http_response import json_http_response
from wgame.manager import get_game_version_switch, set_game_version_switch
from wgame.models import WGameVersion

@csrf_exempt
def version_control_view(request, game_name, version, switch):
    """
    版本控制
    :param request:
    :param game_name: 游戏名称
    :param version: 版本号
    :param switch: 开关
    :return:
    """
    # if request.method == 'GET':
    #     switch_result = get_game_version_switch(game_name, version)
    #     return json_http_response({
    #         "error_code": 0,
    #         "result": switch_result,
    #     })
    # elif request.method == 'POST':
    #     set_game_version_switch(game_name, version, switch)
    #     return json_http_response({
    #         "error_code": 0,
    #     })
    # switch = request.GET.get("switch", "0")
    if request.method == 'GET':
        switch_result = get_game_version_switch(game_name, version)
    elif request.method == 'POST':
        set_game_version_switch(game_name, version, switch)
        switch_result = get_game_version_switch(game_name, version)
    return json_http_response({
        "error_code": 0,
        "game_name": game_name,
        "version": version,
        "switch": switch,
        "result": switch_result,
    })


def get_game_version_view(request):
    """
    获取版本号
    :param request:
    :return:
    """
    game_name = request.GET.get("appCode", "")
    game_version = request.GET.get("appVersion", "")
    if not game_name or not game_version:
        return json_http_response({"error_code":1, "error_msg": u"缺少名称或版本号信息"})
    switch_result = get_game_version_switch(game_name, game_version)
    return json_http_response({
        "error_code": 0,
        "game_name": game_name,
        "version": game_version,
        "switch": switch_result,
    })


def set_game_version_view(request):
    """
    设置版本号
    :param request:
    :return:
    """
    game_name = request.GET.get("appCode", "")
    game_version = request.GET.get("appVersion", "")
    switch = int(request.GET.get("appStatus", "0"))
    if not game_name or not game_version:
        return json_http_response({"error_code": 1, "error_msg": u"缺少名称或版本号信息"})
    set_game_version_switch(game_name, game_version, switch)
    switch_result = get_game_version_switch(game_name, game_version)
    return json_http_response({
        "error_code": 0,
        "game_name": game_name,
        "version": game_version,
        "switch": switch_result,
    })

