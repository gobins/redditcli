from redditcli import client
import pytest
import mock

@pytest.fixture(scope='module')
def httpclient():
    my_client = client.HTTPClient('http://test123', 'asdfdsfsf', 'test-agent')
    return my_client

def test_update_headers(httpclient):
    headers = {'Authorization' : 'asdfafd', 'User-Agent': 'Test Agent'}
    response = httpclient._update_headers(headers)
    assert response is not None

@mock.patch('requests.get')
def test_get_method(httpclient):
    response = httpclient.get('test-url')
    assert response is not None
