import time

class RobloxProcessor:
    def __init__(self):
        self.cache = {}

    def process_data(self, data):
        start_time = time.time()
        # Check if the result is in cache
        if hash(data) in self.cache:
            return self.cache[hash(data)]
        
        # Simulate data processing
        result = self._expensive_operation(data)
        processing_time = time.time() - start_time
        print(f"Processing Time: {processing_time:.4f} seconds")
        # Store result in cache for future use
        self.cache[hash(data)] = result
        return result

    def _expensive_operation(self, data):
        # Simulate an expensive operation
        time.sleep(1)  # simulate delay
        return sum(data)  # replace with actual processing logic

# Usage example
if __name__ == '__main__':
    processor = RobloxProcessor()
    print(processor.process_data([1, 2, 3, 4]))  # First call, not cached
    print(processor.process_data([1, 2, 3, 4]))  # Second call, should use cache
