from pathlib import Path

source = Path("evidence/PS-002_phone/email.txt")
output = Path("extracted_artifacts/extracted_email.txt")

content = source.read_text(encoding="utf-8")

output.write_text(
    "EXTRACTED EMAIL ARTEFACT\n"
    "========================\n\n"
    + content
    + "\n\n"
    "Source: PS-002_phone/email.txt\n"
    "Status: SIMULATED FORENSIC ARTEFACT\n",
    encoding="utf-8"
)

print("Email artefact extracted successfully.")
print(f"Output: {output}")
