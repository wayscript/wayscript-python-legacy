# Copyright (c) 2019 WayScript, Inc. All rights reserved.
# Licensed under the MIT License.

from unittest import TestCase
from unittest.mock import patch

from wayscript import WayScript
from wayscript.exceptions import InvalidApiKeyException, InvalidArgumentException


class TestWayScript( TestCase ):
    DUMMY_API_KEY = "_DUMMY_API_KEY_DUMMY_API_KEY_DUMMY_API_KEY_"
    USERNAME      = 'captain@wayscript.com'
    PASSWORD      = 'letmein'
    PROGRAM_ID    = 1234
    QUERY_PARAMS  = { 'var1': 'one', 'var2': 'two', 'var3': 'three' }
    BODY_PARAMS   = { 'var4': 'four', 'var5': 'five', 'var6': 'six' }
    API_URL       = f'https://{ PROGRAM_ID }.wayscript.io/'
    ENDPOINT      = 'my_endpoint'

    def test_api_key_arg( self ):
        with self.assertRaises( InvalidApiKeyException ):
            WayScript( **{ 'api_key': '' } )

        with self.assertRaises( InvalidApiKeyException ):
            WayScript( **{ 'api_key': 'foobar' } )

        self.assertIsNotNone( WayScript( **{ 'api_key': self.DUMMY_API_KEY } ) )

    def test_username_and_password_args( self ):
        self.assertIsNotNone( WayScript( **{ 'username': self.USERNAME, 'password': self.PASSWORD } ) )

    def test_invalid_arg( self ):
        with self.assertRaises( InvalidArgumentException ):
            WayScript( **{ 'invalid_argument': 'foobar' } )

    def test_get_auth_header( self ):
        wayscript = WayScript( **{ 'username': self.USERNAME, 'password': self.PASSWORD } )
        self.assertEqual( 'Basic Y2FwdGFpbkB3YXlzY3JpcHQuY29tOmxldG1laW4=', wayscript._get_auth_header() )

        wayscript = WayScript( **{ 'api_key': self.DUMMY_API_KEY } )
        self.assertEqual( f'Bearer { self.DUMMY_API_KEY }', wayscript._get_auth_header() )

    def test_run_no_auth( self ):
        wayscript = WayScript()

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID )
            headers = { 'X-WayScript-Api': 'python' }
            post_request.assert_called_once_with( self.API_URL, data = None, headers = headers, params = None )

    def test_run_with_api_key( self ):
        wayscript = WayScript( **{ 'api_key': self.DUMMY_API_KEY } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': f'Bearer { self.DUMMY_API_KEY }' }
            post_request.assert_called_once_with( self.API_URL, data = None, headers = headers, params = None )

    def test_run_with_username_and_password( self ):
        wayscript = WayScript( **{ 'username': self.USERNAME, 'password': self.PASSWORD } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': 'Basic Y2FwdGFpbkB3YXlzY3JpcHQuY29tOmxldG1laW4=' }
            post_request.assert_called_once_with( self.API_URL, data = None, headers = headers, params = None )

    def test_run_custom_endpoint_no_auth( self ):
        wayscript = WayScript()

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = None, headers = headers, params = None )

    def test_run_custom_endpoint_with_api_key( self ):
        wayscript = WayScript( **{ 'api_key': self.DUMMY_API_KEY } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': f'Bearer { self.DUMMY_API_KEY }' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = None, headers = headers, params = None )

    def test_run_custom_endpoint_with_username_and_password( self ):
        wayscript = WayScript( **{ 'username': self.USERNAME, 'password': self.PASSWORD } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': 'Basic Y2FwdGFpbkB3YXlzY3JpcHQuY29tOmxldG1laW4=' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = None, headers = headers, params = None )

    def test_run_no_auth_with_query_params( self ):
        wayscript = WayScript()

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, params = self.QUERY_PARAMS )
            headers = { 'X-WayScript-Api': 'python' }
            post_request.assert_called_once_with( self.API_URL, data = None, headers = headers, params = self.QUERY_PARAMS )

    def test_run_authenticated_with_query_params( self ):
        wayscript = WayScript( **{ 'username': self.USERNAME, 'password': self.PASSWORD } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, params = self.QUERY_PARAMS )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': 'Basic Y2FwdGFpbkB3YXlzY3JpcHQuY29tOmxldG1laW4=' }
            post_request.assert_called_once_with( self.API_URL, data = None, headers = headers, params = self.QUERY_PARAMS )

    def test_run_custom_endpoint_no_auth_with_query_params( self ):
        wayscript = WayScript()

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, params = self.QUERY_PARAMS, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = None, headers = headers, params = self.QUERY_PARAMS )

    def test_run_custom_endpoint_authenticated_with_query_params( self ):
        wayscript = WayScript( **{ 'api_key': self.DUMMY_API_KEY } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, params = self.QUERY_PARAMS, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': f'Bearer { self.DUMMY_API_KEY }' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = None, headers = headers, params = self.QUERY_PARAMS )

    def test_run_no_auth_with_body_params( self ):
        wayscript = WayScript()

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, data = self.BODY_PARAMS )
            headers = { 'X-WayScript-Api': 'python' }
            post_request.assert_called_once_with( self.API_URL, data = self.BODY_PARAMS, headers = headers, params = None )

    def test_run_authenticated_with_body_params( self ):
        wayscript = WayScript( **{ 'username': self.USERNAME, 'password': self.PASSWORD } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, data = self.BODY_PARAMS )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': 'Basic Y2FwdGFpbkB3YXlzY3JpcHQuY29tOmxldG1laW4=' }
            post_request.assert_called_once_with( self.API_URL, data = self.BODY_PARAMS, headers = headers, params = None )

    def test_run_custom_endpoint_no_auth_with_body_params( self ):
        wayscript = WayScript()

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, data = self.BODY_PARAMS, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = self.BODY_PARAMS, headers = headers, params = None )

    def test_run_custom_endpoint_authenticated_with_body_params( self ):
        wayscript = WayScript( **{ 'api_key': self.DUMMY_API_KEY } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, data = self.QUERY_PARAMS, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': f'Bearer { self.DUMMY_API_KEY }' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = self.QUERY_PARAMS, headers = headers, params = None )

    def test_all_params( self ):
        wayscript = WayScript( **{ 'api_key': self.DUMMY_API_KEY } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, params = self.QUERY_PARAMS, data = self.BODY_PARAMS, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': f'Bearer {self.DUMMY_API_KEY}' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = self.BODY_PARAMS, headers = headers,
                                                  params = self.QUERY_PARAMS )

    def test_empty_params( self ):
        wayscript = WayScript( **{ 'api_key': self.DUMMY_API_KEY } )

        with patch( 'requests.post' ) as post_request:
            wayscript.run( self.PROGRAM_ID, params = { }, data = { }, endpoint = self.ENDPOINT )
            headers = { 'X-WayScript-Api': 'python', 'Authorization': f'Bearer {self.DUMMY_API_KEY}' }
            post_request.assert_called_once_with( self.API_URL + self.ENDPOINT, data = { }, headers = headers,
                                                  params = { } )

    def test_returns_response( self ):
        wayscript = WayScript()

        with patch( 'requests.post', return_value = 'ok' ) as post_request:
            response = wayscript.run( self.PROGRAM_ID, params = self.QUERY_PARAMS )
            headers = { 'X-WayScript-Api': 'python' }
            post_request.assert_called_once_with( self.API_URL, data = None, headers = headers, params = self.QUERY_PARAMS )

            self.assertEqual( response, 'ok' )
