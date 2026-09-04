import hashlib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
HASH_FILE = BASE_DIR / "hashes" / "sha256_hashes.txt"

with open(HASH_FILE, "r", encoding="utf-8") as f:
    records = [line.strip() for line in f if line.strip()]

passed = 0
failed = 0

for record in records:
    parts = record.split("  ", 1)
    if len(parts) != 2:
        continue

    expected_hash, relative_path = parts
    file_path = BASE_DIR / relative_path

    if not file_path.exists():
        print(f"FAIL: {relative_path} - file not found")
        failed += 1
        continue

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)

    actual_hash = sha256.hexdigest()

    if actual_hash.lower() == expected_hash.lower():
        print(f"PASS: {relative_path}")
        passed += 1
    else:
        print(f"FAIL: {relative_path}")
        failed += 1

print()
print(f"Passed: {passed}")
print(f"Failed: {failed}")

if failed > 0:
    raise SystemExit(1)
