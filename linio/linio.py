import json
from hmac import HMAC
from urllib import parse
from hashlib import sha256
from datetime import datetime
from logging import basicConfig
from logging import INFO
from logging import info
from logging import warning
from requests import request

basicConfig(level=INFO, format="%(asctime)s - %(levelname)s - %(message)s",
            filename="linio/log/linio.log", filemode="a")


class linio:

    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }

    def __init__(self, user, key, country="co") -> None:
        self.user = user
        self.key = key
        self.endpoint = f"https://sellercenter-api.linio.com.{country}"


    def certificate(self, atts=None):
        """sign the application
            
        Args:
            atts (dict, optional): aditional parameters. Defaults to None.

        Returns:
            dict : return sign params
        """
        params = {
            'UserID': self.user,
            'Version': '1.0',
            'Format': 'JSON',
            'Timestamp': datetime.now().isoformat()
        }

        if atts != None:
            params.update(atts)

        api_key = self.key.encode('utf-8')
        concatenated = parse.urlencode(sorted(params.items())).encode('utf-8')
        params['Signature'] = HMAC(api_key, concatenated, sha256).hexdigest()

        return params


    def query(self, method, params={}, payload={}, headers={}):
        """query method

        Args:
            method (str): select method get, post
            params (dict, optional): parameters. Defaults to {}.
            payload (dict, optional): data. Defaults to {}.
            headers (dict, optional): headers. Defaults to {}.

        Returns:
            dict, None : returns dict answer or None
        """

        response = request(method,
                           url=self.endpoint,
                           data=payload,
                           params=self.certificate(params),
                           headers=headers)

        action = params['Action']

        if response.status_code == 200:

            response_json = json.loads(response.text)

            def status(response_json): return 'SuccessResponse' if 'SuccessResponse' in response_json else 'ErrorResponse'
            info(f"{method} - {action} - {status(response_json)}")

            if status(response_json) == 'ErrorResponse':
                warning(f"{response_json}")
                return None

            return response_json

        warning(f"{method} - {action} - {response.json()['message']}")

        return None
