# -*- coding:utf-8 -*-
"""
{
    game_name: {
        version: switch,
    },
}
"""
GAME_VERSION_SWITCH = {}


def get_game_version_switch(game, version):
    return GAME_VERSION_SWITCH.get(game, {}).get(version, 0)

def set_game_version_switch(game, version, switch):
    game_dict = GAME_VERSION_SWITCH.get(game)
    if not game:
        GAME_VERSION_SWITCH[game] = {}
        game_dict = GAME_VERSION_SWITCH[game]

    game_dict[version] = switch