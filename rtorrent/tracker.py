# Copyright (c) 2011 Chris Lucas, <cjlucas07@gmail.com>
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class Tracker:
    """Represents an individual tracker within a L{Torrent} instance."""
    def __init__(self, _p, info_hash, **kwargs):
        self._p = _p #: X{ServerProxy} instance
        self.info_hash = info_hash #: info hash for the torrent using this tracker
        for k in kwargs.keys():
            setattr(self, k, kwargs.get(k, None))

        # for clarity's sake...
        self.index = self.group #: position of tracker within the torrent's tracker list

    def __repr__(self):
        return("<Tracker url=\"{0}\">".format(self.url))

    def enable(self):
        """Alias for set_enabled("yes")"""
        self.set_enabled("yes")
    def disable(self):
        """Alias for set_enabled("no")"""
        self.set_enabled("no")