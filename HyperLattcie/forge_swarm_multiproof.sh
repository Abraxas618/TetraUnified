
#!/bin/bash
set -e

echo "[🌐] Initializing Swarm Multiproof Engine..."

# Step 1: Generate individual ZK proofs across pods (RTH, QIDL, TetraChain)
echo "[🧠] Generating RTH proof..."
./init_qgd_nexus.sh # Runs QGD oracle and generates input.json for RTH

echo "[🔗] Generating QIDL proof..."
# Send RTH proof output as input for QIDL processing
curl -X POST http://[fd00::3]:8080/zk/prove -H "Content-Type: application/json" --data @input.json

echo "[⚡] Generating TetraChain proof..."
# Send QIDL proof output to final chain anchor
curl -X POST http://[fd00::4]:8080/zk/prove -H "Content-Type: application/json" --data @input.json

# Step 2: Collect and aggregate the proofs into a composite multiproof
echo "[🔒] Aggregating multiproof for final validation..."
multiproof_data=$(curl -X GET http://[fd00::5]:8080/zk/prove -H "Content-Type: application/json")

# Step 3: Package final multiproof for submission to the secure ledger
echo "[💾] Final multiproof generated. Saving to disk..."
echo "$multiproof_data" > final_multiproof.json

# Step 4: Verify multiproof across all chain stages
echo "[🔍] Verifying multiproof across all pods..."
curl -X POST http://[fd00::5]:8080/zk/verify -H "Content-Type: application/json" --data @final_multiproof.json

echo "[✅] Swarm Multiproof Engine Simulation Complete!"
