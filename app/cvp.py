"""
cvp.py
Functions for generating CVP feeds.

:copyright: (C) 2014 by github.com/alfg.
:license:   MIT, see README for more details.
"""

def cvp_player_to_dict(player):
    """
    Convert a player object from a Tree to a CVP-compliant dict.
    """
    return {
        "session": player.session,
        "userid": player.userid,
        "name": player.name,
        "deaf": player.deaf,
        "mute": player.mute,
        "selfDeaf": player.selfDeaf,
        "selfMute": player.selfMute,
        "suppress": player.suppress,
        "onlinesecs": player.onlinesecs,
        "idlesecs": player.idlesecs
    }

def cvp_chan_to_dict(channel):
    """
    Convert a channel from a Tree object to a CVP-compliant dict, recursively.
    """
    return {
        "id": channel.c.id,
        "parent": channel.c.parent,
        "name": channel.c.name,
        "description": channel.c.description,
        "channels": [ cvp_chan_to_dict(chan) for chan in channel.children ],
        "users": [ cvp_player_to_dict(plr) for plr in channel.users ],
        "position": channel.c.position,
        "temporary": channel.c.temporary,
        "links": channel.c.links
    }

def cvp_tree(tree):
    """
    Walk a Tree object returned from a server and convert it to a dict
    in CVP format.
    """

    return {
        "root": cvp_chan_to_dict(tree),
        "name": 'Root',
    }
