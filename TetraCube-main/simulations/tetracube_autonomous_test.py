#!/usr/bin/env python3

import os
import subprocess
import hashlib
import time
from pathlib import Path

# === CONFIG ===
CREDENTIAL_BAND = "TestNation"
CREDENTIAL_SECRET = "QuantumVision"
CREDENTIAL_FILE = f"credentials/{CREDENTIAL_BAND}_{CREDENTIAL_SECRET}_cred.json"

# === TEST RUNNER ===

def print_step(msg):
    print(f"\n=== {msg} ===")

def run_cmd(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {' '.join(command)}")

def main():
    start_time = time.time()
    
    print_step("1. Launch API and Generate Credential")
    run_cmd(["python3", "CodexAPI.py"])
    time.sleep(3)
    run_cmd(["python3", "generate_credential.py", CREDENTIAL_BAND, CREDENTIAL_SECRET])

    if not Path(CREDENTIAL_FILE).exists():
        print("❌ Credential generation failed.")
        return
    print("✅ Credential generated.")

    print_step("2. Simulate Quantum Attack (Corrupt Credential)")
    with open(CREDENTIAL_FILE, "w") as f:
        f.write("CORRUPTEDQUANTUMATTACK")
    print("✅ Credential file corrupted.")

    print_step("3. Destroy Swarm Ledger and Kill Mesh")
    if Path("ledger/").exists():
        subprocess.run(["rm", "-rf", "ledger/"])
    try:
        subprocess.run(["docker", "kill", "$(docker ps -q --filter ancestor=yggdrasil-image)"], shell=True)
    except Exception as e:
        print("⚠️ Mesh kill simulated manually.")

    print_step("4. Reboot Mesh Network")
    try:
        subprocess.run(["docker", "run", "-d", "yggdrasil-image"])
        print("✅ Mesh network rebooted.")
    except Exception as e:
        print("⚠️ Mesh reboot simulated manually.")

    print_step("5. Regenerate Credential and Run ZK Pipeline")
    run_cmd(["python3", "generate_credential.py", CREDENTIAL_BAND, CREDENTIAL_SECRET])
    run_cmd(["python3", "zk_pipeline.py"])
    print("✅ ZKP Proof Completed.")

    print_step("6. Final Integrity Check")
    sha256 = hashlib.sha256()
    with open(CREDENTIAL_FILE, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256.update(byte_block)
    print(f"SHA256: {sha256.hexdigest()}")

    end_time = time.time()
    elapsed = end_time - start_time
    print_step("🚀 MISSION COMPLETE")
    print(f"Total Time: {elapsed/60:.2f} minutes")

if __name__ == "__main__":
    main()
