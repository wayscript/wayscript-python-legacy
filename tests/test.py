# Copyright (c) 2019 WayScript, Inc. All rights reserved.
# Licensed under the MIT License.

from unittest import TestCase
from unittest.mock import patch

from wayscript import WayScript
from wayscript.exceptions import InvalidApiKeyException


class TestWayScript( TestCase ):
    dummy_api_key = "_DUMMY_API_KEY_DUMMY_API_KEY_DUMMY_API_KEY_"
    program_id = 1234
    variables = [ 'one', 'two', 'three' ]
    api_url = 'https://wayscript.com/api'
    headers = { 'X-WayScript-Api': 'python' }

    def test_api_key( self ):
        with self.assertRaises( InvalidApiKeyException ):
            WayScript( '' )

        with self.assertRaises( InvalidApiKeyException ):
            WayScript( 'foobar' )

        self.assertIsNotNone( WayScript( self.dummy_api_key ) )

    def test_run_program( self ):
        wayscript = WayScript( self.dummy_api_key )

        with patch( 'requests.post' ) as post_request:
            wayscript.run_program( self.program_id )
            post_request.assert_called_once_with( self.api_url, params = { 'api_key': self.dummy_api_key,
                                                                  'program_id': self.program_id,
                                                                  'run_async': False },
                                                                headers = self.headers )

    def test_run_program_with_variables( self ):
        wayscript = WayScript( self.dummy_api_key )

        with patch( 'requests.post' ) as post_request:
            wayscript.run_program( self.program_id, variables = self.variables )
            post_request.assert_called_once_with( self.api_url, params = { 'api_key': self.dummy_api_key,
                                                                           'program_id': self.program_id,
                                                                           'run_async': False,
                                                                           'variables': self.variables },
                                                                headers = self.headers )

    def test_run_program_async( self ):
        wayscript = WayScript( self.dummy_api_key )

        with patch( 'requests.post' ) as post_request:
            wayscript.run_program( self.program_id, variables = self.variables, run_async = True )
            post_request.assert_called_once_with( self.api_url, params = { 'api_key': self.dummy_api_key,
                                                                           'program_id': self.program_id,
                                                                           'run_async': True,
                                                                           'variables': self.variables },
                                                                headers = self.headers )

    def test_empty_variables( self ):
        wayscript = WayScript( self.dummy_api_key )

        with patch( 'requests.post' ) as post_request:
            wayscript.run_program( self.program_id, variables = [ ], run_async = True )
            post_request.assert_called_once_with( self.api_url, params = { 'api_key': self.dummy_api_key,
                                                                           'program_id': self.program_id,
                                                                           'run_async': True },
                                                                headers = self.headers )

    def test_returns_response( self ):
        wayscript = WayScript( self.dummy_api_key )

        with patch( 'requests.post', return_value = 'ok' ) as post_request:
            response = wayscript.run_program( self.program_id, run_async = True )
            post_request.assert_called_once_with( self.api_url, params = { 'api_key': self.dummy_api_key,
                                                                           'program_id': self.program_id,
                                                                           'run_async': True },
                                                                headers = self.headers )
            self.assertEqual( response, 'ok' )
