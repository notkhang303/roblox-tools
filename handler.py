import requests
import time
from requests.exceptions import RequestException

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff=2):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming the response is JSON
        except RequestException as e:
            attempt += 1
            if attempt == retries:
                raise NetworkError(f'Failed to fetch data after {retries} attempts') from e
            print(f'Request failed: {e}, retrying in {backoff ** attempt} seconds...')
            time.sleep(backoff ** attempt)  # Exponential backoff

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)