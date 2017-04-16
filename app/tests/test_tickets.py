import unittest
from json import loads
from unittest.mock import MagicMock as Mock
from unittest.mock import patch

# from nose.tools import assert_list_equal
from app.controllers import ticket


def mock(m):
    with open("app/tests/mocks/tickets/{0}.json".format(m)) as mock:
        return mock.read()


class DefaultWidgetSizeTestCase(unittest.TestCase):
    @patch('app.controllers.ticket.requests.get')
    def test_get_one(self, mock_api_call):
        mock_api_call.return_value = Mock(status_code=200, text=mock("raw/ticket"))
        response = ticket.get_one(1)
        self.assertCountEqual(loads(mock("ticket")), loads(response));

    @patch('app.controllers.ticket.requests.get')
    def test_get_one(self, mock_api_call):
        mock_api_call.return_value = Mock(status_code=200, text=mock("raw/ticket_list"))
        response = ticket.get_list()
        self.assertCountEqual(loads(mock("ticket_list")), loads(response));
