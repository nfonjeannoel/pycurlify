# Using Proxy Settings with curl Function

The curl function allows you to specify proxy settings when making HTTP requests using the curl command. Proxy settings
can be provided as a dictionary containing the following keys:

**type: The type of proxy, such as "http" or "socks5" (default is "http").

url: The URL or IP address of the proxy server.

port: The port number to use for the proxy server (default is "8080").

username: The username to use for proxy authentication (optional).

password: The password to use for proxy authentication (optional).**

# Define proxy settings as a dictionary

proxy_settings = {
'type': 'http',
'url': 'proxy.example.com',
'port': '8080',
'username': 'user',
'password': 'pass'
}

# Call the curl function with proxy settings

output = curl("https://example.com", proxy=proxy_settings)
