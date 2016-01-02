import requests
import logging


class HTTPClient(object):
    """
        HTTPClient: Provides wrapper for get/post methods for rest api
    """
    log = logging.getLogger(__name__)

    def __init__(self, base_url, auth_token, user_agent):
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
