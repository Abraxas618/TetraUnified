
import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt

def golden_cos_entropy(n=100):
    phi = (1 + 5 ** 0.5) / 2
    k = np.arange(1, n+1)
    signals = {
        "phi": np.cos(phi * k),
        "linear": np.cos(k),
        "random": np.cos(np.random.uniform(0, 2*np.pi, n))
    }
    entropies = {}
    for key, sig in signals.items():
        hist, _ = np.histogram(sig, bins=20, density=True)
        hist = hist[hist > 0]
        entropies[key] = entropy(hist, base=2)
    return entropies

if __name__ == "__main__":
    e = golden_cos_entropy()
    for k, v in e.items():
        print(f"{k} entropy: {v:.4f}")
