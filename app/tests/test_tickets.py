from unittest.mock import Mock, patch
from app.controllers import ticket
from nose.tools import assert_is_not_none


@patch('app.controllers.ticket.get')
def test_get_tickets(mock_get):

    mock_get.return_value.ok = True
    res = ticket.get(1)
    assert_is_not_none(res)

