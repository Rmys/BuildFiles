#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    #shelltools.unlink("py-compile")
    #shelltools.sym("/bin/true", "%s/py-compile" % get.curDIR())

    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
    	                 --without-python \
    	                 --with-python3")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING*", "README", "NEWS")
