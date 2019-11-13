# [<img src="https://user-images.githubusercontent.com/31461850/53454621-a1b39500-39dc-11e9-9b3c-276451d42437.png" width="155px" alt="WayScript" align="center">](https://wayscript.com) Python SDK

[![PyPI version](https://img.shields.io/pypi/v/wayscript.svg?color=blue)](https://pypi.python.org/pypi/wayscript/) [![CircleCI Status](https://circleci.com/gh/wayscript/wayscript-python/tree/master.svg?style=shield)](https://circleci.com/gh/wayscript/wayscript-python/tree/master)

### A rapid scripting platform for developers.

WayScript allows you to run Python in the cloud, and seamlessly integrate with your favorite APIs.

![Trigger scripts on any event or schedule.](https://user-images.githubusercontent.com/31461850/68791449-30fde880-05fe-11ea-86d1-8dc739cda767.png)

## Installation

```sh
pip install wayscript
```

## Basic Usage

1. Add one or more [HTTP Triggers](https://docs.wayscript.com/library/triggers/http-trigger) to your script.

2. If you have a [password-protected endpoint](https://docs.wayscript.com/library/triggers/http-trigger#password-protect-your-endpoints), obtain your API key or the credentials you would like to use.

3. If you have specified a [custom endpoint](https://docs.wayscript.com/library/triggers/http-trigger#endpoints), you will need to pass the name of that endpoint in your api call.

4. If your HTTP Trigger takes [query parameters](https://docs.wayscript.com/library/triggers/http-trigger#request-query-parameters) and/or [JSON body parameters](https://docs.wayscript.com/library/triggers/http-trigger#request-json-body-parameters), you can pass those as a dictionary using the `params` and/or `data` arguments, respectively. (See [HTTP Trigger Outputs](https://docs.wayscript.com/library/triggers/http-trigger#outputs) for more information.)

5. Run your WayScript programs from your Python code:

```python
from wayscript import WayScript

# Create the WayScript client
wayscript = WayScript()

# If your program requires a password to run, supply those credentials when creating the client
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
kwargs = { 'username': username, 'password': password }
wayscript = WayScript( **kwargs )

# If your program requires a password to run, you can instead supply your API Key when creating the client
kwargs = { 'api_key': 'MY_API_KEY' }
wayscript = WayScript( **kwargs )

# Run a program by id
program_id = 1234
wayscript.run( program_id )

# Pass query parameters for the HTTP Trigger to output (optional)
query_params = { 'var1': 'one', 'var2': 'two', 'var3': 'three' }
wayscript.run( program_id, params = query_params )

# Pass JSON body parameters for the HTTP Trigger to output (optional)
body_params = { 'var4': 'four', 'var5': 'five', 'var6': 'six' }
wayscript.run( program_id, data = body_params )

# Run a custom endpoint (optional)
endpoint = 'my_endpoint'
wayscript.run( program_id, endpoint = endpoint, params = query_params, data = body_params )

# Get the response from the server
response = wayscript.run( program_id )
```

## Run a WayScript program from command line
```sh
PROGRAM_ID=1234

python -c "from wayscript import WayScript; WayScript().run($PROGRAM_ID)"
```

If you don't want to use Python on the command line, you can use `cURL`. (See the [HTTP Trigger Sample Code](https://docs.wayscript.com/library/triggers/http-trigger#sample-code) for an example.)
