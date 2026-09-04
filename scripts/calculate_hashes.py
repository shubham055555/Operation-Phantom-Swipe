import hashlib
from pathlib import Path
from datetime import datetime

EVIDENCE_DIR = Path("../evidence")
OUTPUT_FILE = Path("../hashes/sha256_hashes.txt")

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(1024 * 1024):
            sha256.update(chunk)

    return sha256.hexdigest()

files = sorted(
    file for file in EVIDENCE_DIR.rglob("*")
    if file.is_file()
)

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
    output.write("OPERATION PHANTOM SWIPE\n")
    output.write("SHA-256 EVIDENCE HASH RECORD\n")
    output.write("=" * 70 + "\n")
    output.write(f"Generated: {datetime.now().isoformat()}\n\n")

    for file in files:
        file_hash = calculate_sha256(file)
        relative_path = file.relative_to(EVIDENCE_DIR)

        print(f"{relative_path}")
        print(f"SHA-256: {file_hash}\n")

        output.write(f"File: {relative_path}\n")
        output.write(f"SHA-256: {file_hash}\n")
        output.write("-" * 70 + "\n")

print(f"\nHash record saved to: {OUTPUT_FILE}")
