#!/usr/bin/env python3
import hashlib
import sys
from datetime import datetime

if len(sys.argv) < 3:
    print("[!] Warning: No band_id or secret provided. Using test defaults.")
    band_id = "TestNation"
    secret = "QuantumVision"
else:
    band_id, secret = sys.argv[1], sys.argv[2]

timestamp = datetime.utcnow().isoformat()
hash_input = f"{band_id}{secret}{timestamp}".encode()
credential = hashlib.shake_256(hash_input).hexdigest(32)

print(f"Credential: {credential}\nTimestamp: {timestamp}")
