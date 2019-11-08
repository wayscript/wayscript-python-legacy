# [<img src="https://user-images.githubusercontent.com/31461850/53454621-a1b39500-39dc-11e9-9b3c-276451d42437.png" width="155px" alt="WayScript" align="center">](https://wayscript.com) Python SDK

[![PyPI version](https://img.shields.io/pypi/v/wayscript.svg?color=blue)](https://pypi.python.org/pypi/wayscript/) [![CircleCI Status](https://circleci.com/gh/wayscript/wayscript-python/tree/master.svg?style=shield)](https://circleci.com/gh/wayscript/wayscript-python/tree/master)

### A new way to build software.

* WayScript gives you flexible building blocks to seamlessly integrate, automate and host tools in the cloud. Unlock new potential with drag and drop programming.

* Instantly connect to hundreds of datasets including GitHub, Twitter, databases, ecommerce data, or build your own integration. WayScript can read data from Excel, Google Sheets, and an evergrowing list of third-party APIs.

* Seamlessly migrate to the cloud: Generate interfaces, instantly share, and run via event-based triggering. 

## Installation

```sh
pip install wayscript
```

## Basic Usage

1. Add one or more [HTTP Triggers](https://docs.wayscript.com/library/triggers/http-trigger) to your script.

2. If you have a [password-protected endpoint](https://docs.wayscript.com/library/triggers/http-trigger#password-protect-your-endpoints), obtain your API key or the credentials you would like to use.

3. If you have specified a [custom endpoint](https://docs.wayscript.com/library/triggers/http-trigger#endpoints), you will need the name of that endpoint as well.

4. If your HTTP Trigger takes query parameters and/or JSON Body Parameters, you can pass those as a dictionary of query_params and/or body_params to your program.

5. Run your WayScript programs from your Python code:

```python
from wayscript import WayScript

username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
kwargs = { 'username': username, 'password': password }
wayscript = WayScript( **kwargs )

# Run a program by id
program_id = 1234
wayscript.run( program_id )

# Pass query parameters for the HTTP Trigger to output (optional)
params = { 'var1': 'one', 'var2': 'two', 'var3': 'three' }
wayscript.run( program_id, query_params = params )

# Pass JSON body parameters for the HTTP Trigger to output (optional)
wayscript.run( program_id, body_params = params )

# Run a custom endpoint (optional)
endpoint = 'my_endpoint'
wayscript.run( program_id, endpoint = endpoint, query_params = params )

# Get the response from the server
response = wayscript.run( program_id )
```

## Run a WayScript program from command line
```sh
PROGRAM_ID=1234

python -c "from wayscript import WayScript; WayScript().run_program($PROGRAM_ID)"
```

If you don't want to use Python on the command line, you can use `curl`. (See the WayScript [REST API documentation](https://wayscript.com/documentation/apis/rest_api).)
