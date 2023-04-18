import subprocess


# Define the main function
def curl(url, *args, **kwargs):
    # Check if the url is valid
    if not isinstance(url, str) or not url.startswith("http"):
        raise ValueError("Invalid url")

    # Build the curl command as a list of strings
    command = ["curl", url]

    # If proxy is provided, append the proxy settings to the command list
    if kwargs.get('proxy'):
        # proxy_settings = {
        #     'type': 'http',
        #     'url': 'proxy.example.com',
        #     'port': '8080',
        #     'username': 'my_username',
        #     'password': 'my_password'
        # }
        proxy = kwargs.get('proxy')
        # Check if proxy is a dictionary
        if not isinstance(proxy, dict):
            raise ValueError("Invalid proxy settings")
        # Extract proxy settings from the dictionary
        proxy_type = proxy.get('type', 'http')
        proxy_url = proxy.get('url')
        proxy_port = proxy.get('port', '8080')
        proxy_username = proxy.get('username')
        proxy_password = proxy.get('password')

        # Construct the proxy string
        proxy_string = f"{proxy_type}://{proxy_username}:{proxy_password}@{proxy_url}:{proxy_port}"

        # Append the proxy string to the command list with "-x" flag
        command.extend(["-x", proxy_string])

    for arg in args:
        # Check if the argument is valid
        if not isinstance(arg, str):
            raise ValueError("Invalid argument")
        # Append the argument to the command list
        command.append(arg)

    # Execute the curl command using subprocess.run
    try:
        result = subprocess.run(command, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        # Handle errors and exceptions
        # print(f"Error: {e.returncode}")
        return e.output.decode()
        # print(f"Error: {e.stderr.decode()}")
        # return None

    # Return the output as a string
    return result.stdout.decode()


# Import the shlex module
import shlex

# Import the os module
import os


# Define the from_curl function
def from_curl(file_name, from_file=False, **kwargs):
    if from_file:
        # Check if the file name is valid
        if not isinstance(file_name, str) or not os.path.isfile(file_name):
            raise ValueError("Invalid file name")

        # Open the file and read the curl string
        with open(file_name, "r") as f:
            curl_string = f.read()
    else:
        curl_string = file_name

    # Check if the curl string is valid
    if not isinstance(curl_string, str) or not curl_string.startswith("curl"):
        raise ValueError("Invalid curl string")

    # Split the curl string into a list of tokens using shlex.split
    tokens = shlex.split(curl_string)

    # Extract the url and the arguments from the tokens
    url = tokens[1]
    args = tokens[2:]

    # Call the curl function with the url and arguments
    return curl(url, *args, **kwargs)


def curl_with_options(url, cookies=None, headers=None, data=None, **kwargs):
    # Check if the url is valid
    if not isinstance(url, str) or not url.startswith("http"):
        raise ValueError("Invalid url")

    # Initialize an empty list of arguments
    args = []

    # If cookies are given, format them as a string and append to the arguments list
    if cookies:
        # Check if cookies are a dictionary
        if not isinstance(cookies, dict):
            raise ValueError("Invalid cookies")
        # Join the cookie key-value pairs with "=" and ";" separators
        cookie_string = "; ".join([f"{key}={value}" for key, value in cookies.items()])
        # Append the cookie string to the arguments list with "-b" flag
        args.extend(["-b", cookie_string])

        # If headers are given, format them as a string and append to the arguments list
    if headers:
        # Check if headers are a dictionary
        if not isinstance(headers, dict):
            raise ValueError("Invalid headers")
        # Join the header key-value pairs with ":" and "\r\n" separators
        header_string = "\r\n".join([f"{key}: {value}" for key, value in headers.items()])
        # Append the header string to the arguments list with "-H" flag
        args.extend(["-H", header_string])

    # If data are given, format them as a string and append to the arguments list
    if data:
        # Check if data are a dictionary
        if not isinstance(data, dict):
            raise ValueError("Invalid data")
        # Join the data key-value pairs with "=" and "&" separators
        data_string = "&".join([f"{key}={value}" for key, value in data.items()])
        # Append the data string to the arguments list with "-d" flag
        args.extend(["-d", data_string])

    # Call the curl function with the url and arguments
    return curl(url, *args, **kwargs)
