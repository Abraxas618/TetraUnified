
#!/usr/bin/env python3

import hashlib
import json
import time
import random
from datetime import datetime
import os

def generate_entropy(seed_phrase):
    timestamp = datetime.utcnow().isoformat()
    noise = str(random.getrandbits(512))
    concat = f"{seed_phrase}|{timestamp}|{noise}"
    digest = hashlib.sha512(concat.encode()).hexdigest()
    return digest[:64], timestamp

def encode_zk_oracle(entropy_hash, layers=3):
    zk_seeds = []
    for i in range(layers):
        layer_input = f"{entropy_hash}|layer{i}"
        hashed = hashlib.blake2b(layer_input.encode(), digest_size=32).hexdigest()
        zk_seeds.append(hashed)
    return zk_seeds

def forge_qgd_oracle(seed_phrase):
    print("[QGD] Quantum Gatekeeper Daemon Oracle Activated.")
    entropy, timestamp = generate_entropy(seed_phrase)
    print(f"[QGD] Entropy Base: {entropy}")
    print(f"[QGD] UTC Timestamp: {timestamp}")

    zk_layers = encode_zk_oracle(entropy)
    oracle_packet = {
        "oracle_entropy": entropy,
        "timestamp": timestamp,
        "zk_layers": zk_layers,
        "q_signature": hashlib.sha3_256(entropy.encode()).hexdigest()
    }

    # Save directly to /mnt/data/ to persist outside of the sandbox
    filename = f"/mnt/data/QGD_oracle_packet_{int(time.time())}.json"
    with open(filename, "w") as f:
        json.dump(oracle_packet, f, indent=2)

    print(f"[QGD] Oracle packet forged and saved to: {filename}")
    return filename

if __name__ == "__main__":
    seed = os.getenv("QGD_SEED", "Unimetrix1-Luminal-Anchor")
    forge_qgd_oracle(seed)
