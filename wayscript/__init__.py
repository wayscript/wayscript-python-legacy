# -*- coding: utf-8 -*-

"""
WayScript Python SDK
~~~~~~~~~~~~
This module implements the WayScript Client.
:copyright: (c) 2019 WayScript, Inc
:license: MIT, see LICENSE.txt for more details.
"""

from wayscript.client import Client

class WayScript( Client ):
    """A user-created :class:`WayScript <WayScript>` client object.
        Used to send requests to the WayScript server.
        :param **kwargs: Argument dictionary containing either an API key or username and password.
        Usage::
          >>> from wayscript import WayScript
          >>> kwargs = { 'api_key': 'YOUR_API_KEY'  }
          >>> wayscript = WayScript( **kwargs )
        """
    pass

