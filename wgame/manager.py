# -*- coding:utf-8 -*-
"""
{
    game_name: {
        version: switch,
    },
}
"""
from wgame.models import WGameVersion

GAME_VERSION_SWITCH = {}


def get_game_version_switch(game, version):
    game_version = WGameVersion.objects.filter(game=game, version=version).order_by("-id")[:1]
    return game_version[0].switch if game_version else 0

def set_game_version_switch(game, version, switch):
    game_version = WGameVersion.objects.filter(game=game, version=version).order_by("-id")[:1]
    if not game_version:
        game_version = WGameVersion.objects.create(
            game=game,
            version=version,
            switch=switch,
        )
