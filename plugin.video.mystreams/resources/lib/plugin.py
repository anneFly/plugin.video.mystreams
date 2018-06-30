# -*- coding: utf-8 -*-

import routing
import logging
import xbmcaddon
from xbmc import Player
from xbmcgui import ListItem
from xbmcplugin import (
    addDirectoryItem, endOfDirectory, addSortMethod, SORT_METHOD_LABEL_IGNORE_THE,
    setResolvedUrl, setContent
)
from resources.lib import kodilogging

ADDON = xbmcaddon.Addon()
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()

STREAM_CONFIG = {
    'ard': {
        'name': 'ARD',
        'stream_url': 'https://derste247livede.akamaized.net/hls/live/658317/daserste_de/04cfc76071a513710ef7683ebe3e1add/index_7.m3u8',
    },
    'ard_alpha': {
        'name': 'ARD alpha',
        'stream_url': 'https://brlive-lh.akamaihd.net/i/bralpha_germany@119899/index_3776_av-p.m3u8',
    },
    'arte': {
        'name': 'arte',
        'stream_url': 'https://artelive-lh.akamaihd.net/i/artelive_de@393591/index_1_av-p.m3u8',
    },
    'dw': {
        'name': 'Deutsche Welle',
        'stream_url': 'https://dwstream72-lh.akamaihd.net/i/dwstream72_live@123556/index_1_av-p.m3u8',
    },
    'mdr': {
        'name': 'mdr Sachsen',
        'stream_url': 'https://mdrsnhls-lh.akamaihd.net/i/livetvmdrsachsen_de@513998/index_3776_av-p.m3u8',
    },
    'wdr': {
        'name': 'WDR',
        'stream_url': 'https://wdrfsgeo-lh.akamaihd.net/i/wdrfs_geogeblockt@530016/index_3776_av-p.m3u8',
    },
    '3sat': {
        'name': '3sat',
        'stream_url': 'https://zdf0910-lh.akamaihd.net/i/dach10_v1@392872/index_1496_av-p.m3u8',
    },
    'phoenix': {
        'name': 'phoenix',
        'stream_url': 'https://zdf0910-lh.akamaihd.net/i/de09_v1@392871/index_1496_av-p.m3u8',
    },
    'one': {
        'name': 'One',
        'stream_url': 'https://onelivestream-lh.akamaihd.net/i/one_livestream@568814/index_7_av-p.m3u8'
    },
    'zdf': {
        'name': 'ZDF',
        'stream_url': 'http://zdf1314-lh.akamaihd.net/i/de14_v1@392878/index_3096_av-p.m3u8',
    },
    'zdf_info': {
        'name': 'ZDF Info',
        'stream_url': 'https://zdf1112-lh.akamaihd.net/i/de12_v1@392882/master.m3u8',
    },
    'zdf_neo': {
        'name': 'ZDF neo',
        'stream_url': 'https://zdf1314-lh.akamaihd.net/i/de13_v1@392877/index_3096_av-p.m3u8',
    },
}


@plugin.route('/')
def index():
    setContent(plugin.handle, 'videos')

    for stream_id, conf in STREAM_CONFIG.items():
        title = conf['name']
        video_settings = {
            'title': title,
            'mediatype': 'video',
        }

        list_item = ListItem(label=title)
        list_item.setInfo('video', video_settings)

        addDirectoryItem(
            plugin.handle,
            plugin.url_for(play_video, stream_id),
            list_item,
            isFolder=False,
        )

    addSortMethod(plugin.handle, SORT_METHOD_LABEL_IGNORE_THE)
    endOfDirectory(plugin.handle)


@plugin.route('/<stream_id>')
def play_video(stream_id):
    stream = STREAM_CONFIG[stream_id]
    url = stream['stream_url']
    list_item = ListItem(label=stream['name'], path=url)

    # setResolvedUrl(plugin.handle, True, list_item)
    Player().play(url, list_item)


def run():
    plugin.run()
