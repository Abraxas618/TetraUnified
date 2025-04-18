
from setuptools import setup, find_packages

setup(
    name="tetra_codex",
    version="1.0.0",
    py_modules=["generate_credential", "post_quantum_crypto", "zk_pipeline", "CodexMetrics"],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'codex-cred=generate_credential:main',
            'codex-zk=zk_pipeline:run_pipeline'
        ]
    },
)
