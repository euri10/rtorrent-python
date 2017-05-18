from time import time

import pytest

from rtorrent import RTorrent, Torrent


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

def test_Torrent(socketpath):
    rtorrent = RTorrent(socketpath)
    t = Torrent(rtorrent,info_hash="42B7EFAB0D48757C6D7906272733BD22B57BB182")