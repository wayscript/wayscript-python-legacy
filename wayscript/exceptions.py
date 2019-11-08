# -*- coding: utf-8 -*-

"""
wayscript.exceptions
~~~~~~~~~~~~
This module contains the WayScript exception classes.
:copyright: (c) 2019 WayScript, Inc
:license: MIT, see LICENSE.txt for more details.
"""


class InvalidApiKeyException( Exception ):
    def __init__( self ):
        super().__init__( 'The API Key provided is not valid.' )

class InvalidArgumentException( Exception ):
    def __init__( self, arg: str ):
        super().__init__( f'The argument { arg } is not valid.' )
