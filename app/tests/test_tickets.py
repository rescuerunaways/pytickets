from json import loads
from unittest.mock import MagicMock as Mock
from unittest.mock import patch

from nose.tools import assert_list_equal

from app.controllers.ticket import get_one


def mock(m):
    with open("app/tests/mocks/tickets/{0}.json".format(m)) as mock:
        return mock.read()


@patch('app.controllers.ticket.requests.get')
def test_get_one(mock_api_call):
    mock_api_call.return_value = Mock(status_code=200, text=mock("raw/ticket"))
    response = get_one()
    assert_list_equal(loads(mock("ticket")), loads(response));
