import requests
import logging


class HTTPClient(object):
    """
        HTTPClient: Provides wrapper for get/post methods for rest api
    """
    log = logging.getLogger(__name__)
    
    def __init__(self, base_url, auth_token=None, user_agent=None):
        self.log.debug('Initializing HTTPClient class')
        self.base_url = base_url
        self.auth_token = auth_token
        self.user_agent = user_agent

    def get(self, url, headers=None):
        """Http GET method wrapper"""
        self.log.debug('GET Method: %s', self.base_url+ url)
        headers = self._update_headers(headers)
        resp = requests.get(self.base_url+url, headers=headers)
        return resp

    def _update_headers(self, headers):
        if not headers:
            headers = {}
        auth_token = headers.get('Authorization', self.auth_token)
        if auth_token:
            headers['Authorization'] = 'bearer '+auth_token
        user_agent = headers.get('User-Agent', self.user_agent)
        if user_agent:
            headers['User-Agent'] = user_agent
        return headers

    def post(self, url, body, headers=None, client_auth=None):
        """HTTP POST method wrapper"""
        self.log.debug('POST Method: %s', self.base_url+url)
        headers = self._update_headers(headers)
        content_type = headers.get('content-type', 'application/json')
        headers['content-type'] = content_type
        if client_auth:
            return requests.post(self.base_url+url, auth=client_auth, data=body, headers=headers)
        else:
            return requests.post(self.base_url+url, data=body, headers=headers)


class Client(object):
    """
       Client class for handling authentication
    """
    log = logging.getLogger(__name__)
    def __init__(self, base_url):
        self.log.debug('Initializing Client class')
        self.base_url = base_url

    def get_auth_token(self, auth_url=None, cred=None):
        """Method for retreiving authentication token"""
        self.log.debug('Calling get_auth_token method')
        client_auth = requests.auth.HTTPBasicAuth(
            cred.client_id,
            cred.client_secret
            )

        post_data = {
            'grant_type' : 'password',
            'username': cred.username,
            'password': cred.password
        }

        headers = {
            'User-Agent': 'python-app/0.1 by redditcli'
        }

        httpclient = HTTPClient(base_url=self.base_url)
        return httpclient.post(url=auth_url, body=post_data, headers=headers, client_auth=client_auth)
