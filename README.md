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

1. Get the API Key from your WayScript user profile page

2. Run your WayScript programs from your Python code:

```python
from wayscript import WayScript

api_key = 'YOUR_API_KEY'
wayscript = WayScript( api_key )

# Run a program by id
program_id = 1234
wayscript.run_program( program_id )

# Pass variables to a program (optional)
variables = [ 'one', 'two', 'three' ]
wayscript.run_program( program_id, variables = variables )

# Run a specific function within your program (optional)
function = 'My Function'
wayscript.run_program( program_id, variables = variables, function = function )

# Run a program asynchronously (optional)
wayscript.run_program( program_id, run_async = True )
wayscript.run_program( program_id, variables = variables, function = function, run_async = True )

# Get the response from the server
response = wayscript.run_program( program_id )
```

⭐ In order to run a program using the WayScript Python API, you must first add an active [Webhook Trigger](https://wayscript.com/documentation/trigger/webhook_trigger) to that program.

### Running a specific function

- The function you specify MUST have an active [Webhook Trigger](https://wayscript.com/documentation/trigger/webhook_trigger).
- If you do not specify a function name in your request and your program has ***one*** function with a Webhook Trigger, the function with the Webhook Trigger will run.
- If you do not specify a function name in your request and your program has ***multiple*** functions with Webhook Triggers, you will be asked to specify which function you would like to run.

## Run a WayScript program from command line
```sh
WS_API_KEY="YOUR_API_KEY"
PROGRAM_ID=1234
ARGUMENT="whatever"
FUNCTION="My Function"

python -c "from wayscript import WayScript; WayScript('$WS_API_KEY').run_program($PROGRAM_ID, '$ARGUMENT', '$FUNCTION')"
```

If you don't want to use Python on the command line, you can use `curl`. (See the WayScript [REST API documentation](https://wayscript.com/documentation/apis/rest_api).)
