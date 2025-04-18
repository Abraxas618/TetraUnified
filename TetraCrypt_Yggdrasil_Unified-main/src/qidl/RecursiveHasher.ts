// QIDL Recursive Hasher – Final Codex-Class Edition
import crypto from 'crypto';

/**
 * Generates secure salt using high-entropy randomness + precise time.
 */
export function generateEntropySalt(length: number = 16): string {
  const raw = crypto.randomBytes(32).toString('hex') + Date.now().toString();
  const hashed = crypto.createHash('sha256').update(raw).digest('hex');
  return hashed.slice(0, length);
}

/**
 * Recursive QIDL hasher using entropy and loop-based round markers.
 * @param input - Seed string or message
 * @param depth - Recursion depth
 * @param salt - Optional salt (auto-generated if omitted)
 * @returns Codex-hardened QIDL hash
 */
export function recursiveHash(
  input: string,
  depth: number = 6,
  salt?: string
): string {
  const effectiveSalt = salt ?? generateEntropySalt();
  let hashInput = `${input}-${effectiveSalt}-${Date.now()}`;  // Initial entropy pulse

  for (let i = 0; i < depth; i++) {
    const hash = crypto.createHash('sha256');
    hash.update(`${hashInput}-round-${i}`);  // Round-specific variation
    hashInput = hash.digest('hex');
  }

  return `QIDL-${hashInput.slice(0, 32)}`;
}
