import requests

from hubspot import exceptions
from hubspot.enums import ErrorEnum
from hubspot.companies import Companies
from hubspot.contact_lists import ContactLists
from hubspot.contacts import Contacts
from hubspot.deals import Deals
from hubspot.fields import Fields
from hubspot.integrations import Integrations
from hubspot.webhooks import Webhooks
from hubspot.workflows import Workflows
from urllib.parse import urlencode, urlparse


class Client(object):
    BASE_URL = "https://api.hubapi.com/"

    def __init__(self, app_id, hapikey, client_id, client_secret):
        self.app_id = app_id
        self.hapikey = hapikey
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

        self.companies = Companies(self)
        self.contact_lists = ContactLists(self)
        self.contacts = Contacts(self)
        self.deals = Deals(self)
        self.fields = Fields(self)
        self.integrations = Integrations(self)
        self.webhooks = Webhooks(self)
        self.workflows = Workflows(self)

    def authorization_url(self, redirect_uri, scope):
        if not isinstance(scope, list):
            raise Exception("scope must be a list.")
        params = {"client_id": self.client_id, "redirect_uri": redirect_uri, "scope": " ".join(scope)}
        url = "https://app.hubspot.com/oauth/authorize?" + urlencode(params)
        return url

    def exchange_code(self, redirect_uri, code):
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": redirect_uri,
            "code": code,
        }
        return self._post("oauth/v1/token", data=data)

    def refresh_token(self, refresh_token):
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
        }
        return self._post("oauth/v1/token", data=data)

    def set_access_token(self, access_token):
        self.access_token = access_token

    def _get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def _post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def _put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def _request(self, method, endpoint, headers=None, params=None, **kwargs):
        _headers = {"Authorization": "Bearer {}".format(self.access_token)}
        if params and "hapikey" in params:
            del _headers["Authorization"]
        if headers:
            _headers.update(headers)
        return self._parse(
            requests.request(method, self.BASE_URL + endpoint, headers=_headers, params=params, **kwargs)
        )

    def _parse(self, response):
        print(response.request.url)
        if "Content-Type" in response.headers and "application/json" in response.headers["Content-Type"]:
            r = response.json()
        else:
            r = response

        if not response.ok:
            code = response.status_code
            message = r.get("message", None)
            try:
                error_enum = ErrorEnum(code)
            except Exception:
                raise exceptions.UnexpectedError("{}".format(message))

            if error_enum == ErrorEnum.Unauthorized:
                raise exceptions.UnauthorizedError(message)
            elif error_enum == ErrorEnum.Forbidden:
                raise exceptions.ForbiddenError(message)
            elif error_enum == ErrorEnum.TooManyRequests:
                raise exceptions.TooManyRequestsError(message)
            elif error_enum == ErrorEnum.Timeout1:
                raise exceptions.TimeoutError(message)
            elif error_enum == ErrorEnum.Timeout2:
                raise exceptions.TimeoutError(message)
            elif error_enum == ErrorEnum.NotFound:
                raise exceptions.NotFoundError(message)
            elif error_enum == ErrorEnum.MethodNotAllowed:
                raise exceptions.MethodNotAllowedError(message)
            else:
                raise exceptions.BaseError("{}".format(message))

        return r
