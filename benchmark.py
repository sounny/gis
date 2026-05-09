import time
import unittest
from tests.test_link_integrity import TestLinkIntegrity

def run_benchmark(iterations=100):
    test = TestLinkIntegrity('test_local_links_exist')
    start_time = time.time()
    for _ in range(iterations):
        try:
            test.test_local_links_exist()
        except AssertionError:
            # We expect an assertion error if there are broken links, but the loop still runs.
            pass
    end_time = time.time()
    print(f"Time for {iterations} iterations: {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    run_benchmark()
