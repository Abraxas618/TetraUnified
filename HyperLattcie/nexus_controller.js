
const express = require('express');
const { execSync } = require('child_process');
const fs = require('fs');

const app = express();
app.use(express.json());

app.post('/zk/prove', (req, res) => {
  const { entropy_seed, saltA, saltB, saltC, saltD } = req.body;
  const input = {
    entropy_seed: entropy_seed.toString(),
    saltA: saltA.toString(),
    saltB: saltB.toString(),
    saltC: saltC.toString(),
    saltD: saltD.toString()
  };

  fs.writeFileSync('input.json', JSON.stringify(input, null, 2));

  try {
    execSync('node TetraCodex_QuantumChain_js/generate_witness.js TetraCodex_QuantumChain_js/TetraCodex_QuantumChain.wasm input.json witness.wtns');
    execSync('snarkjs groth16 prove full_proof.zkey witness.wtns proof.json public.json');
    const result = execSync('snarkjs groth16 verify verification_key.json public.json proof.json').toString();
    res.send({ status: 'OK', proof_result: result });
  } catch (e) {
    res.status(500).send({ status: 'ERROR', message: e.toString() });
  }
});

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`[🌐] Nexus API server listening on port ${PORT}`);
});
