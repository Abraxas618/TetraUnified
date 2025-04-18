
const express = require('express');
const { execSync } = require('child_process');

const app = express();
app.use(express.json());

app.post('/generate-proof', (req, res) => {
  const { entropy, salt1, salt2, salt3 } = req.body;

  const input = {
    entropy: entropy.toString(),
    salt1: salt1.toString(),
    salt2: salt2.toString(),
    salt3: salt3.toString()
  };

  const fs = require('fs');
  fs.writeFileSync('input.json', JSON.stringify(input, null, 2));

  try {
    execSync('node rth_qidl_chain_js/generate_witness.js rth_qidl_chain_js/rth_qidl_chain.wasm input.json witness.wtns');
    execSync('snarkjs groth16 prove full_proof.zkey witness.wtns proof.json public.json');
    const result = execSync('snarkjs groth16 verify verification_key.json public.json proof.json').toString();
    res.send({ status: 'OK', result });
  } catch (e) {
    res.status(500).send({ status: 'FAIL', error: e.toString() });
  }
});

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`ZK Proof Controller running on port ${PORT}`);
});
