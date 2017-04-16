import unittest
from json import loads

from app.services import processor


def mock(m):
    with open("app/tests/mocks/tickets/{0}.json".format(m)) as mock:
        return mock.read()


class ProcessorTestCase(unittest.TestCase):
    def test_process_one(self):
        processed = processor.process_one(mock("raw/ticket"))
        self.assertCountEqual(loads(mock("ticket")), loads(processed))

    def test_process_list(self):
        processed_list = processor.process_list(mock("raw/ticket_list"))
        self.assertCountEqual(loads(mock("ticket_list")), loads(processed_list))
