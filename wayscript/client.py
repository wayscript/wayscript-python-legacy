# -*- coding: utf-8 -*-

"""
wayscript.client
~~~~~~~~~~~~
This module handles WayScript API calls.
:copyright: (c) 2019 WayScript, Inc
:license: MIT, see LICENSE.txt for more details.
"""

import requests
from wayscript.exceptions import InvalidApiKeyException


class Client:
    def __init__( self, api_key):
        if not api_key or len( api_key ) != 43:
            raise InvalidApiKeyException()

        self._api_key = api_key
        self._api_url = 'https://wayscript.com/api'

    def run_program( self, program_id, variables = None, run_async = False ):
        """Runs a WayScript program.
            :param program_id: The id of the program you want to run.
            :param variables: (optional) An array of arguments to pass to your program.
            :param run_async: (optional) Run this program asyncronously.
                    If False, this command will block until your program has finished running.
            :return: Response object
            :rtype: requests.Response
            Usage::
                >>> from wayscript import WayScript
                >>> api_key = 'YOUR_API_KEY'
                >>> wayscript = WayScript( api_key )
                >>> program_id = 1234
                >>> response = wayscript.run_program( program_id, variables = variables, run_async = True )
              <Response [200]>
            """

        params = { 'api_key': self._api_key,
                   'program_id': program_id,
                   'run_async': run_async }

        if variables and len( variables ):
            params[ 'variables' ] = variables

        return self._post( params )

    def _post( self, params ):
        return requests.post( self._api_url, params = params )
