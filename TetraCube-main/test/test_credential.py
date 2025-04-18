#!/usr/bin/env python3
# TetraCube Sovereign Cryptography Test Suite
# Author: Michael Tass MacDonald (Abraxas618)
# Version: v1.0 (2025)

import sys
import os
import unittest
from datetime import datetime

# === Path Resolver ===
# Allow relative import from project root (TetraCube/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# === Import Target Modules ===
from post_quantum_crypto import pq_hash, generate_entropy_key

# === Unit Test Suite ===

class TestPostQuantumCrypto(unittest.TestCase):
    """Test post-quantum cryptographic primitives integrity."""

    def test_pq_hash_output_length(self):
        """Ensure pq_hash outputs exactly 64 characters."""
        hashed = pq_hash("test_input", "test_salt")
        self.assertEqual(len(hashed), 64, "Hash output length mismatch.")

    def test_pq_hash_deterministic(self):
        """Ensure pq_hash is deterministic given same input."""
        a = pq_hash("static", "salted")
        b = pq_hash("static", "salted")
        self.assertEqual(a, b, "Hash is not deterministic with same input.")

    def test_entropy_key_length(self):
        """Ensure generated entropy keys are correct length."""
        key = generate_entropy_key(64)
        self.assertEqual(len(key), 64, "Entropy key length mismatch.")

    def test_entropy_key_randomness(self):
        """Ensure two generated entropy keys are not identical."""
        key1 = generate_entropy_key(64)
        key2 = generate_entropy_key(64)
        self.assertNotEqual(key1, key2, "Entropy keys should differ.")

# === Entry Point ===

if __name__ == "__main__":
    start_time = datetime.utcnow()
    print(f"Running TetraCube Sovereign Test Suite — {start_time.isoformat()} UTC\n")
    unittest.main(verbosity=2)
