from time import time

import pytest

from rtorrent import RTorrent


@pytest.fixture
def socketpath():
    # return 'scgi:///home/lotso/.local/share/lxc/torrent/rootfs/home/rtorrent/.rtorrent.sock'
    return 'scgi:///home/lotso/.rtorrent.sock'

def test_RTorrent(socketpath):
    rtorrent = RTorrent(socketpath)
    assert rtorrent.test_connection() is True
    listViews = rtorrent.get_views()
    print(listViews)
    t0= time()
    listTorrents = rtorrent.get_torrents()
    t1 = time()
    print(listTorrents, t1-t0)
    listTorrents = rtorrent.get_torrents()
    t2 = time()
    print(listTorrents,  t2-t1)