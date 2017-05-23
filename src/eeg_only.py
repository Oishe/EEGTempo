from liblo import *

import sys
import time

# muse-io --device '00:06:66:6B:F7:3F' --osc 'osc.udp://localhost:5000'

class MuseServer(ServerThread):
    #listen for messages on port 5000
    def __init__(self):
        ServerThread.__init__(self, 5000)

        # #handle unexpected messages
        # @make_method(None, None)
        # def fallback(self, path, args, types, src):
        #     print "Unknown message \
        #     \n\t Source: '%s' \
        #     \n\t Address: '%s' \
        #     \n\t Types: '%s ' \
        #     \n\t Payload: '%s'" \
        #     % (src.url, path, types, args)

    #receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print "%s %f %f %f %f" % (path, l_ear, l_forehead, r_forehead, r_ear)


try:
    server = MuseServer()
except ServerError, err:
    print str(err)
    sys.exit()


server.start()

if __name__ == "__main__":
    while 1:
        time.sleep(1)
