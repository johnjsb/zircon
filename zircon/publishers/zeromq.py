"""

"""

import zmq
import cPickle as pickle

from zircon.publishers.base import BasePublisher


class ZMQPublisher(BasePublisher):

    def __init__(self, host='*', port=8811, zmq_type=zmq.PUB):

        self.host = host
        self.port = port
        self.zmq_type = zmq_type
        self.URI = 'tcp://{}:{}'.format(self.host, self.port)

        self.context = zmq.Context()
        self.sock = self.context.socket(self.zmq_type)

        self.count = 0

    def open(self):
        self.sock.bind(self.URI)
        return True

    def close(self):
        self.sock.close()
        return True

    def send(self, msg):

        try:
            self.sock.send(msg)
            self.count += 1
            print('[SENT] {}'.format(self.count))
        except TypeError:
            print('[ERROR] Message fed to Publisher must be serialized!')
            return False

        return True
