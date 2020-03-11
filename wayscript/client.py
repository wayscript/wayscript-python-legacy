# -*- coding: utf-8 -*-

"""
wayscript.client
~~~~~~~~~~~~
This module handles WayScript API calls.
:copyright: (c) 2019 WayScript, Inc
:license: MIT, see LICENSE.txt for more details.
"""

import base64, requests
from urllib import parse

from wayscript.exceptions import InvalidApiKeyException, InvalidArgumentException


class Client:
    def __init__( self, **kwargs ):
        self._api_key = self._username = self._password = None

        for key, value in kwargs.items():
            if key.lower() == 'api_key':
                if not value or len( value ) != 43:
                    raise InvalidApiKeyException()
                self._api_key = value
            elif key.lower() == 'username':
                self._username = value
            elif key.lower() == 'password':
                self._password = value
            else:
                raise InvalidArgumentException( key )

    def run( self, program_id: int, endpoint: str = '', params: dict = None, data: dict = None ):
        """Runs a WayScript program.
            :param program_id: The id of the program you want to run.
            :param endpoint: (optional) The name of the HTTP Trigger endpoint that you would like to run.
            :param params: (optional) An dictionary of query parameters to pass to your program.
            :param data: (optional) An dictionary of JSON body parameters to pass to your program.
            :return: Response object
            :rtype: requests.Response
            Usage::
                >>> from wayscript import WayScript
                >>>
                >>> kwargs = { 'api_key': 'YOUR_API_KEY' }
                >>> wayscript = WayScript( **kwargs )
                >>>
                >>> program_id = 1234
                >>> endpoint = 'my_endpoint'
                >>> query_params = { 'var1': 'one', 'var2': 'two', 'var3': 'three' }
                >>> body_params = { 'bodyVar1': 'hello', 'bodyVar2': 'world' }
                >>> response = wayscript.run( program_id, endpoint = endpoint, params = query_params, data = body_params )
              <Response [200]>
            """

        headers = { 'X-WayScript-Api': 'python' }
        auth_header = self._get_auth_header()
        if auth_header: headers[ 'Authorization' ] = auth_header

        url = f'https://{ program_id }.wayscript.io/' + parse.quote( endpoint or '' )

        return requests.post( url, params = params, data = data, headers = headers )

    def _get_auth_header( self ):
        if self._api_key:
            return 'Bearer ' + self._api_key
        elif self._username and self._password:
            return 'Basic ' + Client._encode_str( f'{ self._username }:{ self._password }' )
        else:
            return None

    @staticmethod
    def _encode_str( string: str ):
        return base64.b64encode( bytes( string, 'utf-8' ) ).decode( 'utf-8' )
