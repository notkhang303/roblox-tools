import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    """
    Makes a network request to the specified URL with retry logic.
    Retries the request if a RequestException occurs.
    
    Parameters:
        url (str): The URL to request.
        max_retries (int): Maximum number of retries. Default is 3.
        delay (int): Delay in seconds between retries. Default is 2.
    
    Returns:
        Response object if successful, None if not.
    """
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            return response
        except RequestException as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                time.sleep(delay)
    return None
