import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff=1):
    """Makes a GET request with retry logic."""
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return JSON response if successful
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(backoff)
                backoff *= 2  # Exponential backoff
                continue  # Retry the request
            raise NetworkError(f'Network request failed after {retries} attempts: {e}') from e

# Example usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)