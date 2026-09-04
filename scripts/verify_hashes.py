import hashlib
from pathlib import Path

EVIDENCE_DIR = Path("../evidence")
HASH_FILE = Path("../hashes/sha256_hashes.txt")

def sha256(file_path):
    h = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)

    return h.hexdigest()

records = {}

current_file = None

with open(HASH_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if line.startswith("File: "):
            current_file = line[6:]

        elif line.startswith("SHA-256: ") and current_file:
            records[current_file] = line[9:]
            current_file = None

print("OPERATION PHANTOM SWIPE")
print("EVIDENCE INTEGRITY VERIFICATION")
print("=" * 60)

passed = 0
failed = 0

for relative_path, expected_hash in records.items():

    file_path = EVIDENCE_DIR / relative_path

    if not file_path.exists():
        print(f"[MISSING] {relative_path}")
        failed += 1
        continue

    actual_hash = sha256(file_path)

    if actual_hash == expected_hash:
        print(f"[PASS] {relative_path}")
        passed += 1
    else:
        print(f"[FAIL] {relative_path}")
        failed += 1

print("\n" + "=" * 60)
print(f"Passed: {passed}")
print(f"Failed: {failed}")

if failed == 0:
    print("RESULT: ALL EVIDENCE INTEGRITY CHECKS PASSED")
else:
    print("RESULT: INTEGRITY CHECK FAILED")
