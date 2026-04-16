import random
import string

def generate_random_username(length=8):
    """Generate a random username of given length."""
    if length < 3:
        raise ValueError('Length must be at least 3 characters')
    letters = string.ascii_letters + string.digits
    username = ''.join(random.choice(letters) for _ in range(length))
    return username


def validate_username(username):
    """Check if a username is valid based on criteria."""
    if not username:
        return False
    if len(username) < 3 or len(username) > 20:
        return False
    if not username.isalnum():
        return False
    return True


def format_database_connection_string(host, port, db_name, user, password):
    """Construct a database connection string."""
    return f'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'


def is_valid_email(email):
    """Validate email format using regex."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
