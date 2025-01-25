import time

def test_performance():
    start_time = time.time()
    # Simulating system load (e.g., content generation)
    time.sleep(1)
    assert time.time() - start_time < 2  # Ensure system performs within 2 seconds
