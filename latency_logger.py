import time
import random

def log_latency():
    # Simulate network latency
    latency = random.randint(50, 200)  # ms
    time.sleep(latency / 1000)
    return latency
