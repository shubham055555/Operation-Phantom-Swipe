# Operation Phantom Swipe

## Investigating a Cross-Border ATM & Credit Card Fraud Ring

**Assignment:** Unit 1 – Foundations of Digital Forensics

**Type:** Academic Digital Forensics Simulation

## Project Overview

Operation Phantom Swipe is an academic simulation of an early-stage digital-forensics investigation involving a simulated cross-border ATM skimming and online credit-card fraud operation.

The project demonstrates evidence preservation, chain of custody, SHA-256 hashing, forensic searching, metadata analysis, artefact extraction, password-testing simulation, and legal-ethical analysis.

**All evidence in this repository is synthetic and created exclusively for academic purposes.**

## Investigation Objectives

- Cybercrime classification and taxonomy
- ATM skimming and payment-card fraud analysis
- Electronic evidence acquisition simulation
- Chain-of-custody documentation
- SHA-256 integrity verification
- Keyword/string-based forensic searching
- Metadata analysis
- Email artefact extraction
- GPS and transaction artefact analysis
- Controlled password-testing simulation
- Legal and ethical analysis
- Cross-border investigation considerations
- GitHub Actions repository validation

## Simulated Evidence

### PS-001 – ATM Skimmer

Contains simulated:
- Captured card data
- Skimmer device information
- Skimmer activity logs

### PS-002 – Suspect Mobile Phone

Contains simulated:
- Device information
- Email communication
- GPS records
- Transaction records

No real financial credentials, payment-card information, or private third-party data are included.

## Repository Structure

Operation-Phantom-Swipe/
- evidence/
- generated_data/
- extracted_artifacts/
- hashes/
- chain_of_custody/
- crypto/
- scripts/
- screenshots/
- report/
- README.md
- .github/workflows/validate.yml

## Tools Used

- Python 3
- PowerShell
- 7-Zip
- SHA-256
- Microsoft Word
- Git
- GitHub Actions

## Forensic Scripts

Run from the project root:

python scripts/calculate_hashes.py

python scripts/verify_hashes.py

python scripts/forensic_search.py

python scripts/metadata_analysis.py

python scripts/email_extraction.py

python scripts/dictionary_simulation.py

## Evidence Integrity

SHA-256 hashes are generated for the simulated evidence files and subsequently verified using the verification script.

## Chain of Custody

Chain-of-custody records are stored in:

chain_of_custody/chain_of_custody.txt

chain_of_custody/chain_of_custody.csv

## Cryptography Simulation

A password-protected ZIP archive is included under:

crypto/phantom_protected.zip

The password-testing activity is a controlled academic simulation using synthetic evidence.

## Legal and Ethical Analysis

The technical-legal report discusses:

- Information Technology Act, 2000
- Historical IPC mapping
- Bharatiya Nyaya Sanhita, 2023
- Bharatiya Sakshya Adhiniyam, 2023
- Budapest Convention
- Cross-border evidence challenges
- Lawful access and preservation
- Password-testing ethics

## Final Report

report/Operation_Phantom_Swipe_Technical_Legal_Report.docx

## Academic Authorship Declaration

The evidence dataset, forensic artefacts, analysis scripts, and documentation were prepared for academic purposes.

All simulated evidence is synthetic.

The project does not contain real payment-card information, credentials, or private data belonging to third parties.

## Disclaimer

This repository is an educational digital-forensics simulation.

The project must not be used to access, test, or interfere with systems, accounts, or devices without proper authorization.
