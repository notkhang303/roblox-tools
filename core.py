import time

class RobloxOptimizer:
    def __init__(self, data):
        self.data = data
        self.cache = {}

    def expensive_operation(self, item):
        time.sleep(1)  # Simulating expensive calculation
        return item * 2

    def process_data(self):
        results = []
        for item in self.data:
            if item in self.cache:
                results.append(self.cache[item])
            else:
                result = self.expensive_operation(item)
                self.cache[item] = result
                results.append(result)
        return results

# Example usage:
if __name__ == '__main__':
    optimizer = RobloxOptimizer([1, 2, 3, 1, 2, 3])
    start_time = time.time()
    optimized_results = optimizer.process_data()
    end_time = time.time()
    print(f'Optimized Results: {optimized_results}')
    print(f'Time taken: {end_time - start_time} seconds')