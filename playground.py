#!/usr/bin/env python3
import gi
import signal
import logging
import sys
import os

gi.require_version('Gtk', '3.0')
gi.require_version('Gst', '1.0')

import lib.connection as Connection
from lib.loghandler import LogHandler
from lib.args import Args
from gi.repository import Gtk, Gdk, Gst, GObject
def testCallback(args):
    log = logging.getLogger("Test")
    log.info(str(args))


def main():
    docolor = (Args.color == 'always') or (Args.color == 'auto' and
                                           sys.stderr.isatty())
    loghandler = LogHandler(docolor, Args.timestamp)
    logging.root.addHandler(loghandler)
    if Args.verbose >= 2:
        level = logging.DEBUG
    elif Args.verbose == 1:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.root.setLevel(level)
    logging.debug('setting SIGINT handler')
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Connection.establish(Args.host)
    Connection.enterNonblockingMode()
    Connection.on("test", testCallback)


if __name__ == '__main__':
    main()