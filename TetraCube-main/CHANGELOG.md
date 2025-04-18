# TetraCube DRDC-Proof Changelog

## v1.0.0 - April 17, 2025

### 🚀 Initial Public Release

This release includes the full DRDC-proof cryptographic ecosystem:

#### ✅ Core Features
- `generate_credential.py`: Zero-knowledge voter identity generator
- `post_quantum_crypto.py`: Post-quantum entropy hashing engine
- `zk_pipeline.py`: Circuit build + proof + verifier runner
- `CodexAPI.py`: REST API for credential and entropy endpoints
- `CodexMetrics.py`: Shannon entropy benchmarking (Golden Ratio, Random, Linear)
- `setup.py`: CLI installation entry point
- `README.md`: Launch instructions and module descriptions
- `CHANGELOG.md`: You're reading it

#### 📁 Project Structure
- `zk/`: Placeholder circuits and scripts (auto-failsafe if missing)
- `test/`: Unit tests for crypto methods
- `simulations/`: Golden Ratio entropy visualizer
- `TetraCodex-main/`: Full docs, circuits, DRDC whitepaper, research artifacts

#### 🔐 Security & Stability
- `.gitignore` to exclude pycache and dev clutter
- All core scripts patched for graceful failure and offline usability

---

### 🔖 SHA256 Fingerprint (v1.0.0)
```text
TetraCube_DRDC_Proof.tar.gz
SHA256: 6fc9525b06a8c5c636cfc431c1b8c3f88c058f538c7ae5573640e588fd5d3a1e
```

This release is validated for submission to DRDC, CSE, or public GitHub deployments.
