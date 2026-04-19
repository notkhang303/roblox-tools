import time
from typing import List, Dict

class PerformanceProcessor:
    def __init__(self):
        self.data_cache: Dict[str, List[int]] = {}

    def process_data(self, data: List[int]) -> List[int]:
        if not data:
            return []
        key = self._generate_key(data)
        if key in self.data_cache:
            return self.data_cache[key]
        start_time = time.time()
        result = self._compute_heavy_operation(data)
        elapsed_time = time.time() - start_time
        print(f"Processing time: {elapsed_time:.4f} seconds")
        self.data_cache[key] = result
        return result

    def _generate_key(self, data: List[int]) -> str:
        return ','.join(map(str, sorted(data)))

    def _compute_heavy_operation(self, data: List[int]) -> List[int]:
        # Simulate a time-consuming task
        return [x * 2 for x in data]

# Example Usage
data_processor = PerformanceProcessor()
result = data_processor.process_data([1, 2, 3, 4])
print(result)
result = data_processor.process_data([4, 3, 2, 1])  # Cached result
print(result)