"""

"""

import time
from threading import Thread

from zircon.tranceivers.dummy import DummyTranceiver
from zircon.publishers.zeromq import ZMQPublisher
from zircon.subscribers.zeromq import ZMQSubscriber
from zircon.datastores.dummy import DummyDatastore

from zircon.reporters.base import Reporter
from zircon.injectors.base import Injector

from zircon.transformers.common import *


def launch_reporter_thread():

    def run_reporter():

        reporter = Reporter(
            tranceiver=DummyTranceiver(
                data=range(10),
                dt=0.3
            ),
            transformers=[Combiner(2), Pickler(), Compressor()],
            publisher=ZMQPublisher()
        )
        reporter.run()

    reporter_thread = Thread(target=run_reporter)
    reporter_thread.daemon = True
    reporter_thread.start()


def launch_injector_thread():

    def run_injector():

        injector = Injector(
            subscriber=ZMQSubscriber(),
            transformers=[Decompressor(), Unpickler()],
            datastore=DummyDatastore()
        )
        injector.run()

    injector_thread = Thread(target=run_injector)
    injector_thread.daemon = True
    injector_thread.start()


launch_reporter_thread()
launch_injector_thread()

while True:
    time.sleep(0.1)
