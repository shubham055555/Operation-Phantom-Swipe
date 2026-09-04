from pathlib import Path
from datetime import datetime

EVIDENCE_DIR = Path("evidence")
OUTPUT_FILE = Path("extracted_artifacts/metadata_report.txt")

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    output.write("OPERATION PHANTOM SWIPE\n")
    output.write("SIMULATED FORENSIC METADATA REPORT\n")
    output.write("=" * 70 + "\n\n")

    for file_path in sorted(EVIDENCE_DIR.rglob("*")):

        if not file_path.is_file():
            continue

        stat = file_path.stat()

        created = datetime.fromtimestamp(stat.st_ctime)
        modified = datetime.fromtimestamp(stat.st_mtime)
        accessed = datetime.fromtimestamp(stat.st_atime)

        output.write(f"File: {file_path}\n")
        output.write(f"Extension: {file_path.suffix}\n")
        output.write(f"Size: {stat.st_size} bytes\n")
        output.write(f"Created: {created}\n")
        output.write(f"Modified: {modified}\n")
        output.write(f"Accessed: {accessed}\n")
        output.write("-" * 70 + "\n")

print("Metadata analysis completed.")
print(f"Report saved to: {OUTPUT_FILE}")
