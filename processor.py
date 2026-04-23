from typing import List, Any


def process_data(data: List[Any]) -> List[Any]:
    """
    Processes the input data list by applying some transformations.

    Args:
        data (List[Any]): A list of input data to be processed.

    Returns:
        List[Any]: A list of processed data after transformations.
    """
    processed = []
    for item in data:
        transformed_item = transform_item(item)
        processed.append(transformed_item)
    return processed


def transform_item(item: Any) -> Any:
    """
    A helper function to transform a single item.

    Args:
        item (Any): The input item to be transformed.

    Returns:
        Any: The transformed item.
    """
    # For example, we could just return the item directly (or modify it)
    return item


if __name__ == '__main__':
    sample_data = [1, 2, 3]
    result = process_data(sample_data)
    print(result)  # Expected output: [1, 2, 3]