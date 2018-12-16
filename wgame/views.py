# -*- coding:utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from wgame.http_response import json_http_response
from wgame.manager import get_game_version_switch, set_game_version_switch

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
