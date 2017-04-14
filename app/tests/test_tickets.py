from json import loads
from unittest.mock import patch

from nose.tools import assert_list_equal

from app.services.processor import process_one


def mock(m):
    with open("pytickets/app/tests/mocks/tickets/{0}.json".format(m)) as mock:
        return mock.read()


@patch('app.controllers.ticket.requests.get')
def test_process_one(mock_get):
    raw_ticket = mock("raw/ticket")
    processed_ticket = process_one(raw_ticket)
    ticket = mock("ticket")

    assert_list_equal(loads(processed_ticket), loads(ticket))
