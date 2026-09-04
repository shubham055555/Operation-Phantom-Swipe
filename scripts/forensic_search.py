from pathlib import Path
from datetime import datetime

EVIDENCE_DIR = Path("evidence")
OUTPUT_FILE = Path("extracted_artifacts/forensic_search_report.txt")

KEYWORDS = [
    "card",
    "transaction",
    "gps",
    "location",
    "email",
    "payment",
    "skimmer",
    "password"
]

print("=" * 70)
print("OPERATION PHANTOM SWIPE")
print("FORENSIC STRING SEARCH")
print("=" * 70)

results = []

for file_path in sorted(EVIDENCE_DIR.rglob("*")):

    if not file_path.is_file():
        continue

    try:
        content = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )
    except Exception:
        continue

    lines = content.splitlines()

    for line_number, line in enumerate(lines, start=1):

        for keyword in KEYWORDS:

            if keyword.lower() in line.lower():

                result = (
                    str(file_path),
                    line_number,
                    keyword,
                    line.strip()
                )

                results.append(result)

                print(
                    f"[FOUND] {keyword} | "
                    f"{file_path} | "
                    f"Line {line_number}"
                )

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT_FILE, "w", encoding="utf-8") as output:

    output.write("OPERATION PHANTOM SWIPE\n")
    output.write("FORENSIC STRING SEARCH REPORT\n")
    output.write("=" * 70 + "\n")
    output.write(
        f"Search Time: {datetime.now().isoformat()}\n\n"
    )

    output.write("SEARCH KEYWORDS\n")
    output.write("-" * 70 + "\n")

    for keyword in KEYWORDS:
        output.write(f"- {keyword}\n")

    output.write("\nSEARCH RESULTS\n")
    output.write("-" * 70 + "\n")

    for file_path, line_number, keyword, line in results:

        output.write(
            f"File: {file_path}\n"
            f"Line: {line_number}\n"
            f"Keyword: {keyword}\n"
            f"Content: {line}\n"
            + "-" * 70 + "\n"
        )

    output.write(
        f"\nTotal matches: {len(results)}\n"
    )

print()
print("=" * 70)
print(f"Total matches found: {len(results)}")
print(f"Report saved to: {OUTPUT_FILE}")
print("=" * 70)
