from utils.tx_simulation import simulate_transaction
from utils.latency_logger import log_latency
import json

def main():
    print("🚀 Raiku Demo Tool Starting...")
    
    # Dummy transaction data
    tx_data = {"sender": "Alice", "receiver": "Bob", "amount": 10}
    
    # Simulate transaction
    result = simulate_transaction(tx_data)
    print("Transaction Result:", result)
    
    # Log latency
    latency = log_latency()
    print("Transaction Latency:", latency, "ms")
    
    # Save transaction result to JSON
    with open("data/sample_tx.json", "w") as f:
        json.dump(result, f, indent=2)
    print("Transaction result saved to data/sample_tx.json")

if __name__ == "__main__":
    main()
