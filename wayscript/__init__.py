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
        :param api_key: The API Key for a WayScript account.
        Usage::
          >>> from wayscript import WayScript
          >>> api_key = 'YOUR_API_KEY'
          >>> wayscript = WayScript( api_key )
        """
    pass

