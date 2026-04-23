from typing import Dict, Any

class DataProcessor:
    def __init__(self, data: Dict[str, Any]) -> None:
        """Initialize the processor with data.

        Args:
            data (Dict[str, Any]): The data to be processed.
        """
        self.data = data

    def filter_data(self, criteria: Dict[str, Any]) -> Dict[str, Any]:
        """Filter the data based on given criteria.

        Args:
            criteria (Dict[str, Any]): Filtering criteria.

        Returns:
            Dict[str, Any]: Filtered data.
        """
        return {key: value for key, value in self.data.items() if all(item in value.items() for item in criteria.items())}

    def sort_data(self, key: str, reverse: bool = False) -> Dict[str, Any]:
        """Sort the data based on a given key.

        Args:
            key (str): The key to sort by.
            reverse (bool): Sort in descending order if True.

        Returns:
            Dict[str, Any]: Sorted data.
        """
        return dict(sorted(self.data.items(), key=lambda item: item[1].get(key, ''), reverse=reverse))

    def process(self, criteria: Dict[str, Any], sort_key: str, reverse: bool = False) -> Dict[str, Any]:
        """Process the data by filtering and sorting.

        Args:
            criteria (Dict[str, Any]): Criteria for filtering data.
            sort_key (str): The key to sort the results.
            reverse (bool): Sort in descending order if True.

        Returns:
            Dict[str, Any]: Processed data after filtering and sorting.
        """
        filtered_data = self.filter_data(criteria)
        return self.sort_data(sort_key, reverse)