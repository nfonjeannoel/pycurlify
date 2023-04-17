# py-curlify

py-curl is a Python file that allows you to make HTTP requests using curl syntax. It uses the subprocess module to
execute curl commands and returns the output as a string. It also handles errors and exceptions.

## Installation

you can download the source code from GitHub and install it manually:

```bash
git clone https://github.com/user/py-curlify.git

```

## Usage

To use py-curlify, you need to import it and call the `curl` function with the desired url and arguments. For example:

```python
# Import the package
import py_curl

# Call the curl function with a url
output = py_curl.curl("https://example.com")

# Print the output
print(output)

# Call the curl function with a url and arguments
output = py_curl.curl("https://example.com", "-X", "POST", "-d", "name=John")

# Print the output
print(output)
```

You can also use the `from_curl` function to parse a curl string and execute it. For example:

```python
# Import the package
import py_curl

# Define a curl string
curl = 'curl https://example.com -X POST -H "Content-Type: application/json" -d "{\"name\":\"John\"}"'

# Call the from_curl function with the curl string
output = py_curl.from_curl(curl)

# Print the output
print(output)
```

You can also use the `curl_with_options` function to make a request with cookies, headers, and data as dictionaries. For
example:

```python
# Import the package
import py_curl

# Define the url
url = "https://example.com"

# Define the cookies
cookies = {
    "session": "123456"
}

# Define the headers
headers = {
    "User-Agent": "py-curlify"
}

# Define the data
data = {
    "name": "John"
}

# Call the curl_with_options function with the url and options
output = py_curl.curl_with_options(url, cookies=cookies, headers=headers, data=data)

# Print the output
print(output)
```

## License

py-curlify is created by Jean-Noel in partnership with Chatgpt :)