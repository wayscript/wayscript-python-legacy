# -*- coding: utf-8 -*-

"""
wayscript.client
~~~~~~~~~~~~
This module handles WayScript API calls.
:copyright: (c) 2019 WayScript, Inc
:license: MIT, see LICENSE.txt for more details.
"""

import base64, requests

from wayscript.exceptions import InvalidApiKeyException, InvalidArgumentException


class Client:
    def __init__( self, **kwargs ):
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


    def run( self, program_id: int, params: dict = None, endpoint: str = '' ):
        """Runs a WayScript program.
            :param program_id: The id of the program you want to run.
            :param params: (optional) An dictionary of parameters to pass to your program.
            :param endpoint: (optional) The name of the HTTP Trigger endpoint that you would like to run.
            :return: Response object
            :rtype: requests.Response
            Usage::
                >>> from wayscript import WayScript
                >>> wayscript = WayScript( { 'api_key': 'YOUR_API_KEY' } )
                >>> program_id = 1234
                >>> params = { 'var1': 'one', 'var2': 'two', 'var3': 'three' }
                >>> endpoint = 'my_endpoint'
                >>> response = wayscript.run( program_id, params = params, endpoint = endpoint )
              <Response [200]>
            """

        headers = { 'X-WayScript-Api': 'python' }
        auth_header = self._get_auth_header()
        if auth_header: headers[ 'Authentication' ] = auth_header

        url = f'https://{ program_id }.wayscript.com/' + ( endpoint or '' )

        return requests.post( url, params = params, headers = headers )

    def _get_auth_header( self ):
        if self._api_key:
            return 'Bearer ' + self._api_key
        elif self._username and self._password:
            return 'Basic ' + base64.b64encode( bytes( f'{ self._username }:{ self._password }', 'utf-8' ) ).decode( 'utf-8' )
        else:
            return None
