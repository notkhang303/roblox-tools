import random
import string
from typing import List, Any

def generate_unique_id(length: int = 8) -> str:
    """Generate a unique identifier string."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def find_item_in_list(item: Any, items: List[Any]) -> bool:
    """Check if an item exists in a list."""
    return item in items


def sort_dict_by_key(input_dict: dict) -> dict:
    """Sort a dictionary by its keys."""
    return dict(sorted(input_dict.items()))


def convert_to_camel_case(snake_str: str) -> str:
    """Convert a snake_case string to camelCase."""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def flatten_list(nested_list: List[List[Any]]) -> List[Any]:
    """Flatten a nested list into a single list."""
    return [item for sublist in nested_list for item in sublist]