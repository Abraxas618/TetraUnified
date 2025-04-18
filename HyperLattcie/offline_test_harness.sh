
#!/bin/bash
set -e

echo "[🧪] TetraCodex Quantum Nexus Ultra – Offline Test Harness"
echo "[🔐] Step 1: Compile circuit"
circom TetraCodex_QuantumNexus_Ultra.circom --r1cs --wasm --sym -l ./circomlib/circuits

echo "[🔒] Step 2: Powers of Tau + Trusted Setup"
snarkjs powersoftau new bn128 12 pot12_0000.ptau -v
snarkjs powersoftau contribute pot12_0000.ptau pot12_final.ptau --name="Offline Contributor" -v
snarkjs groth16 setup TetraCodex_QuantumNexus_Ultra.r1cs pot12_final.ptau full_proof.zkey
snarkjs zkey export verificationkey full_proof.zkey verification_key.json

echo "[🧠] Step 3: Generate witness"
node TetraCodex_QuantumNexus_Ultra_js/generate_witness.js TetraCodex_QuantumNexus_Ultra_js/TetraCodex_QuantumNexus_Ultra.wasm input.json witness.wtns

echo "[📜] Step 4: Generate ZK proof"
snarkjs groth16 prove full_proof.zkey witness.wtns proof.json public.json

echo "[🔎] Step 5: Verify proof"
snarkjs groth16 verify verification_key.json public.json proof.json

echo "[✅] SUCCESS: Offline Proof Verified – Simulation Complete"
