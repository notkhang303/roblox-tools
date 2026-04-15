import time

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        start_time = time.time()
        results = [self._optimize(item) for item in self.data]
        elapsed_time = time.time() - start_time
        print(f"Processing completed in {elapsed_time:.2f} seconds")
        return results

    def _optimize(self, item):
        # Example optimization: simple multiplication
        return item * 2


if __name__ == '__main__':
    sample_data = range(1000000)
    processor = DataProcessor(sample_data)
    processed_data = processor.process_data()
