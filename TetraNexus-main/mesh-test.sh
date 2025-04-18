
#!/bin/bash

echo "[*] Sending test entropy to RTH node..."
curl -X POST fd00::2:8080/generate-proof -H "Content-Type: application/json" -d '{
  "entropy": 123456,
  "salt1": 111111,
  "salt2": 222222,
  "salt3": 333333
}'
