
import os
import subprocess
from pathlib import Path

def run_pipeline():
    cwd = Path(__file__).parent / "zk"
    if not cwd.exists():
        print("[ZK Pipeline] zk/ folder not found. Creating placeholder.")
        cwd.mkdir(exist_ok=True)
    os.chdir(cwd)

    compile_script = cwd / "compile.sh"
    verify_script = cwd / "verify.sh"

    if not compile_script.exists():
        compile_script.write_text("echo 'Compiling... placeholder'")
    if not verify_script.exists():
        verify_script.write_text("echo 'Verifying... placeholder'")

    steps = [
        ["bash", "compile.sh"],
        ["bash", "verify.sh"]
    ]

    for step in steps:
        try:
            result = subprocess.run(step, capture_output=True, text=True)
            print(f"$ {' '.join(step)}")
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
        except Exception as e:
            print(f"Execution error: {e}")

if __name__ == "__main__":
    run_pipeline()
