#!/usr/bin/env python3

import signal
import logging
import sys



from gi.repository import GObject

GObject.threads_init()
import time

from lib.args import Args
from lib.loghandler import LogHandler
import lib.connection as Connection

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
    Connection.on("message", testCallback)
    while True:
        logging.debug("mimimi...")
        time.sleep(10)


if __name__ == '__main__':
    main()