# -*- coding:utf-8 -*-
"""
{
    game_name: {
        version: switch,
    },
}
"""
from wgame.models import WGameVersion, WGameParam

GAME_VERSION_SWITCH = {}


def get_game_version_switch(game, version):
    game_version = WGameVersion.objects.filter(game=game, version=version).order_by("-id")[:1]
    return game_version[0].switch if game_version else 0

def set_game_version_switch(game, version, switch):
    game_version_qs = WGameVersion.objects.filter(game=game, version=version).order_by("-id")[:1]
    if not game_version_qs:
        game_version = WGameVersion.objects.create(
            game=game,
            version=version,
            switch=int(switch),
        )
    else:
        game_version = game_version_qs[0]
    game_version.switch = int(switch)
    game_version.save()


def get_game_param(game, version):
    game_version = WGameParam.objects.filter(game=game, version=version).order_by("-id")[:1]
    return game_version[0].param if game_version else 0

def set_game_version(game, version, param):
    game_version_qs = WGameParam.objects.filter(game=game, version=version).order_by("-id")[:1]
    if not game_version_qs:
        game_version = WGameParam.objects.create(
            game=game,
            version=version,
            param=param,
        )
    else:
        game_version = game_version_qs[0]
    game_version.param = param
    game_version.save()

