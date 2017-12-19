import requests
from .contacts import Contacts
from .companies import Companies
from .deals import Deals
from .fields import Fields
from hubspot.enumerator import ErrorEnum
from hubspot import exception

"""
The client module is responsible for abstracting away connecting to, making
requests to, and serializing responses from the HubSpot API.
"""


class Client(object):
    def __init__(self, access_token):
        self._base_url = "https://api.hubapi.com/"
        self._access_token = access_token
        self.contacts = Contacts(self)
        self.companies = Companies(self)
        self.deals = Deals(self)
        self.fields = Fields(self)

    def _get(self, endpoint, params=None):
        return self._request('GET', endpoint, params=params)

    def _post(self, endpoint, json=None, aditional_data=None, params=None):
        return self._request('POST', endpoint, json=json, aditional_data=aditional_data, params=params)

    def _delete(self, endpoint):
        return self._request('DELETE', endpoint)

    def _request(self, method, endpoint, json=None, params=None, aditional_data=None):
        headers = {'Authorization': 'Bearer {0}'.format(self._access_token),
                   }
        if aditional_data is not None:
            headers = aditional_data
        response = requests.request(method, self._base_url + endpoint, headers=headers, json=json, params=params)
        return self._parse(response)

    def get_refresh_token(self, data):
        """
        Refresh a token
        :param data: A dictionary with the parameters
        data = {
            "client_id": String
            "client_secret": String
            "redirect_uri": String
            "refresh_token": Sting
        }
        :return: A json
        """
        endpoint = "oauth/v1/token"
        if 'client_id' not in data:
            raise KeyError('The refresh token must have a client_id')
        if 'client_secret' not in data:
            raise KeyError('The refresh token must have a client_secret')
        if 'redirect_uri' not in data:
            raise KeyError('The refresh token must have a redirect_uri')
        if 'refresh_token' not in data:
            raise KeyError('The refresh token must have a refresh_token')
        data['grant_type'] = 'refresh_token'
        aditional_data = {'Content-Type': 'application/x-www-form-urlencoded',
                          'charset': 'utf-8'}
        return self._post(endpoint=endpoint, params=data, aditional_data=aditional_data)

    def _parse(self, response):
        if not response.ok:
            try:
                data = response.json()
                if 'message' in data:
                    code = response.status_code
                    message = data['message']
                else:
                    message = ""
                    code = response.status_code
            except:
                message = ""
                code = response.status_code
            try:
                error_enum = ErrorEnum(code)
            except Exception:
                raise exception.UnexpectedError('Error {0} . Message{1}'.format(code, message))
            if error_enum == ErrorEnum.Unauthorized:
                raise exception.Unauthorized(message)
            elif error_enum == ErrorEnum.Forbidden:
                raise exception.Forbidden(message)
            elif error_enum == ErrorEnum.TooManyRequests:
                raise exception.TooManyRequests(message)
            elif error_enum == ErrorEnum.Timeouts_1:
                raise exception.Timeouts_1(message)
            elif error_enum == ErrorEnum.Timeouts_2:
                raise exception.Timeouts_2(message)
            elif error_enum == ErrorEnum.NotFound:
                raise exception.NotFound(message)
            elif error_enum == ErrorEnum.MethodNotAllowed:
                raise exception.MethodNotAllowed(message)
            else:
                raise exception.BaseError('Error {0} . Message{1}'.format(code, message))
            return data
        else:
            return response
