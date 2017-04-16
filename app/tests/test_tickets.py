import unittest
from unittest.mock import MagicMock as Mock
from unittest.mock import patch

from app.errors.err_handlers import is_ok


class TicketsTestCase(unittest.TestCase):
    @patch('app.controllers.ticket.requests.get')
    def test_get_error(self, mock_api_call):
        mock_api_call.return_value = Mock(ok=False)
        self.assertRaises(Exception, is_ok, mock_api_call.return_value)

    @patch('app.controllers.ticket.requests.get')
    def test_get_ok(self, mock_api_call):
        mock_api_call.return_value = Mock(ok=True)
        self.assertIsNone(is_ok(mock_api_call.return_value))
