
#!/bin/bash
set -e

echo "[🧠] Initializing QGD Oracle..."
python3 forge_qgd_oracle.py

# Extract latest oracle JSON filename
oracle_file=$(ls -t QGD_oracle_packet_*.json | head -n 1)
echo "[🔗] Oracle packet located: $oracle_file"

# Parse JSON to extract seed for Nexus input
entropy=$(jq -r '.oracle_entropy' "$oracle_file")
saltA=$(jq -r '.zk_layers[0]' "$oracle_file" | tr -dc '0-9' | cut -c1-6)
saltB=$(jq -r '.zk_layers[1]' "$oracle_file" | tr -dc '0-9' | cut -c1-6)
saltC=$(jq -r '.zk_layers[2]' "$oracle_file" | tr -dc '0-9' | cut -c1-6)
saltD=$(echo $entropy | tr -dc '0-9' | cut -c1-6)

# Build input JSON for Nexus Ultra
cat <<EOF > input.json
{
  "entropy_seed": $((0x$(echo $entropy | cut -c1-12))),
  "saltA": $saltA,
  "saltB": $saltB,
  "saltC": $saltC,
  "saltD": $saltD
}
EOF

echo "[🚀] Nexus Ultra input.json forged from QGD oracle:"
cat input.json

echo "[🌐] Submitting to Nexus API at fd00::5:8080/zk/prove..."
curl -X POST http://[fd00::5]:8080/zk/prove -H "Content-Type: application/json" --data @input.json
