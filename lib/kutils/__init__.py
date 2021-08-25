# -*- coding: utf8 -*-

# Copyright (C) 2016 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

from kutils.kodiaddon import Addon
addon = Addon()

from kutils.listitem import ListItem, VideoItem, AudioItem
from kutils.itemlist import ItemList
from kutils.actionhandler import ActionHandler
from kutils.busyhandler import busyhandler as busy
from kutils.kodilogging import KodiLogHandler, config
from kutils.dialogbaselist import DialogBaseList
from kutils.localdb import LocalDB
from kutils.player import VideoPlayer

local_db = LocalDB()
player = VideoPlayer()