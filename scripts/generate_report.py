from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path

OUTPUT = Path("report/Operation_Phantom_Swipe_Technical_Legal_Report.docx")

doc = Document()

# -------------------------------------------------
# PAGE SETUP
# -------------------------------------------------

section = doc.sections[0]
section.top_margin = Inches(0.75)
section.bottom_margin = Inches(0.75)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

styles = doc.styles

styles["Normal"].font.name = "Arial"
styles["Normal"].font.size = Pt(10.5)

styles["Title"].font.name = "Arial"
styles["Title"].font.size = Pt(22)

styles["Heading 1"].font.name = "Arial"
styles["Heading 1"].font.size = Pt(15)

styles["Heading 2"].font.name = "Arial"
styles["Heading 2"].font.size = Pt(12)

# -------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------

def add_heading(text, level=1):
    doc.add_heading(text, level=level)

def add_paragraph(text="", bold_prefix=None):
    p = doc.add_paragraph()

    if bold_prefix and text.startswith(bold_prefix):
        r = p.add_run(bold_prefix)
        r.bold = True
        p.add_run(text[len(bold_prefix):])
    else:
        p.add_run(text)

    p.paragraph_format.space_after = Pt(6)
    return p

def shade_cell(cell, fill="D9EAF7"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)

def add_table(headers, rows):

    table = doc.add_table(
        rows=1,
        cols=len(headers)
    )

    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"

    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = header
        shade_cell(cell)

        for run in cell.paragraphs[0].runs:
            run.bold = True

    for row in rows:
        cells = table.add_row().cells

        for i, value in enumerate(row):
            cells[i].text = str(value)

    doc.add_paragraph()

# -------------------------------------------------
# TITLE PAGE
# -------------------------------------------------

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

run = p.add_run("\nOPERATION PHANTOM SWIPE")
run.bold = True
run.font.size = Pt(24)

p.add_run(
    "\n\nInvestigating a Cross-Border ATM & Credit Card Fraud Ring"
).bold = True

p.add_run(
    "\n\nTechnical-Legal Digital Forensics Report"
)

p.add_run(
    "\n\nAssignment 1 – Unit 1: Foundations of Digital Forensics"
)

p.add_run(
    "\n\nAcademic Simulation"
)

p.add_run(
    "\n\nPrepared by: Digital Forensic Investigator"
)

p.add_run(
    "\nDate: September 2026"
)

doc.add_page_break()

# -------------------------------------------------
# EXECUTIVE SUMMARY
# -------------------------------------------------

add_heading("1. Executive Summary")

add_paragraph(
    "Operation Phantom Swipe is an academic simulation of an early-phase "
    "digital-forensics investigation involving an alleged cross-border "
    "ATM skimming and online credit-card fraud operation."
)

add_paragraph(
    "The simulated investigation involves two evidence sources: a simulated "
    "ATM skimmer identified as PS-001 and a simulated suspect mobile phone "
    "identified as PS-002. The evidence dataset contains synthetic card "
    "records, device logs, email communication, GPS records, transaction "
    "records, application metadata and network activity."
)

add_paragraph(
    "The investigation demonstrates foundational forensic processes including "
    "evidence preservation, chain of custody, SHA-256 hashing, string search, "
    "metadata examination, artefact extraction and controlled password-testing "
    "simulation."
)

add_paragraph(
    "All evidence used in this project is synthetic and was created solely "
    "for academic purposes. The project does not target real accounts, "
    "devices, financial information or computer systems."
)

# -------------------------------------------------
# INCIDENT OVERVIEW
# -------------------------------------------------

add_heading("2. Incident Overview")

add_paragraph(
    "The simulated incident represents a criminal group using an ATM skimming "
    "device to capture payment-card information and subsequently using the "
    "captured information in fraudulent online transactions."
)

add_paragraph(
    "The investigation is described as cross-border because relevant digital "
    "evidence may be distributed across different jurisdictions. This creates "
    "additional challenges involving evidence preservation, lawful access, "
    "international cooperation and jurisdiction."
)

add_heading("2.1 Simulated Evidence Sources", 2)

add_table(
    ["Evidence ID", "Device", "Description"],
    [
        ["PS-001", "ATM Skimmer", "Simulated card-data and device activity evidence"],
        ["PS-002", "Mobile Phone", "Simulated application, email, GPS and transaction evidence"],
    ]
)

# -------------------------------------------------
# CYBERCRIME CLASSIFICATION
# -------------------------------------------------

add_heading("3. Cybercrime Classification and Taxonomy")

add_paragraph(
    "The scenario contains three primary cybercrime categories."
)

add_table(
    ["Crime", "Classification", "Digital Footprint", "Justification"],
    [
        [
            "ATM Skimming",
            "Financial cybercrime / payment-card data theft",
            "Skimmer information, card records, device logs",
            "Represents unauthorized capture of payment-card information."
        ],
        [
            "Credit Card Cloning",
            "Payment-card fraud / identity-related misuse",
            "Card records, transactions, communications",
            "Represents fraudulent use of captured payment-card information."
        ],
        [
            "Online Credit Card Fraud",
            "Computer-related financial fraud",
            "Transactions, emails, network and application logs",
            "Represents fraudulent online financial activity."
        ],
    ]
)

add_paragraph(
    "The taxonomy demonstrates that cybercrime can involve both attacks "
    "against computer-related resources and traditional crimes enabled or "
    "facilitated through digital technologies."
)

# -------------------------------------------------
# DIGITAL FOOTPRINT
# -------------------------------------------------

add_heading("4. Digital Footprint and Artefacts")

add_paragraph(
    "The simulated investigation produced multiple artefact categories. "
    "These artefacts were correlated to reconstruct a basic activity timeline."
)

add_table(
    ["Artefact", "Source", "Finding", "Investigative Value"],
    [
        ["A-001", "captured_card_data.txt", "Simulated card records", "Payment-card evidence"],
        ["A-002", "skimmer_log.txt", "Simulated card-capture activity", "Skimming timeline"],
        ["A-003", "email.txt", "Transaction-related communication", "Communication evidence"],
        ["A-004", "gps_log.txt", "Simulated coordinates", "Location evidence"],
        ["A-005", "transaction_log.txt", "Simulated transactions", "Financial activity"],
        ["A-006", "app_metadata.txt", "PaymentHelper metadata", "Application evidence"],
        ["A-007", "application_activity.log", "Application events", "Activity timeline"],
        ["A-008", "network_log.txt", "Simulated network activity", "Network evidence"],
    ]
)

# -------------------------------------------------
# EVIDENCE ACQUISITION
# -------------------------------------------------

add_heading("5. Electronic Evidence Acquisition")

add_paragraph(
    "Two simulated evidence sources were created to represent the seized "
    "ATM skimmer and suspect mobile phone. The evidence was preserved before "
    "forensic analysis."
)

add_heading("5.1 Write Blocking", 2)

add_paragraph(
    "In a real forensic acquisition, a hardware or appropriate software "
    "write blocker can be used to prevent unintended modification of the "
    "original storage media. This supports preservation of evidence integrity."
)

add_heading("5.2 Forensic Copies", 2)

add_paragraph(
    "Forensic examination should preferably be conducted against an acquired "
    "forensic copy rather than modifying the original evidence source."
)

add_heading("5.3 SHA-256 Integrity Verification", 2)

add_paragraph(
    "SHA-256 hashes were generated for seven simulated evidence files. "
    "The hashes were subsequently recalculated and compared against the "
    "recorded values. All simulated integrity checks passed."
)

add_table(
    ["Evidence", "Hash Method", "Verification"],
    [
        ["PS-001 files", "SHA-256", "PASS"],
        ["PS-002 files", "SHA-256", "PASS"],
    ]
)

# -------------------------------------------------
# CHAIN OF CUSTODY
# -------------------------------------------------

add_heading("6. Chain of Custody")

add_paragraph(
    "A chain-of-custody record was created to document the simulated "
    "collection, handling, transfer and preservation of evidence."
)

add_table(
    ["Transfer", "From", "To", "Purpose", "Integrity"],
    [
        ["T-001", "Digital Forensic Investigator", "Forensic Analyst", "Forensic examination", "Verified"],
        ["T-002", "Digital Forensic Investigator", "Forensic Analyst", "Forensic examination", "Verified"],
        ["T-003", "Forensic Analyst", "Evidence Storage", "Secure preservation", "Verified"],
        ["T-004", "Forensic Analyst", "Evidence Storage", "Secure preservation", "Verified"],
    ]
)

add_paragraph(
    "Evidence handling should be restricted to authorized personnel and "
    "each transfer should be documented. Hash verification provides an "
    "additional mechanism for demonstrating that the acquired files have "
    "not changed between examination stages."
)

# -------------------------------------------------
# FORENSIC SEARCH
# -------------------------------------------------

add_heading("7. Forensic Search and Analysis")

add_paragraph(
    "A keyword-based forensic search was performed across the simulated "
    "evidence directory. Search terms included card, transaction, GPS, "
    "location, email, payment, skimmer and password."
)

add_paragraph(
    "The search process recorded the source file, matching keyword, line "
    "number and matching content. This provides a reproducible search trail."
)

add_heading("7.1 Metadata Analysis", 2)

add_paragraph(
    "Basic filesystem metadata was collected for the simulated evidence "
    "files, including filename, extension, file size and filesystem "
    "timestamps. Metadata can assist investigators in establishing an "
    "activity timeline, although timestamps should be interpreted carefully."
)

add_heading("7.2 Email Extraction", 2)

add_paragraph(
    "A simulated email artefact was extracted from PS-002. The email "
    "contained communication concerning a simulated transaction batch."
)

# -------------------------------------------------
# CRYPTOGRAPHY
# -------------------------------------------------

add_heading("8. Cryptography Investigation")

add_paragraph(
    "A password-protected ZIP archive was created containing synthetic "
    "forensic artefacts. A controlled dictionary simulation was performed "
    "against a predefined synthetic password."
)

add_paragraph(
    "The dictionary simulation located the password Phantom2026! after "
    "seven candidate attempts."
)

add_heading("8.1 Ethical Considerations", 2)

add_paragraph(
    "Password testing must only be performed with appropriate authorization "
    "and for a legitimate forensic purpose. Investigators should follow "
    "applicable legal procedures before attempting to access protected "
    "evidence."
)

add_heading("8.2 Password Strength", 2)

add_paragraph(
    "Common and predictable passwords are more susceptible to dictionary "
    "attacks. Longer and less predictable passwords increase the search "
    "space and make guessing more difficult."
)

# -------------------------------------------------
# LEGAL ANALYSIS
# -------------------------------------------------

add_heading("9. Legal and Regulatory Analysis")

add_paragraph(
    "The legal mapping in this academic project is based on the assignment "
    "requirements and official legal sources. Exact criminal liability "
    "depends on the facts, intent, jurisdiction and applicable procedural law."
)

add_heading("9.1 Information Technology Act, 2000", 2)

add_table(
    ["Provision", "General Relevance"],
    [
        [
            "Section 43",
            "Addresses specified unauthorized acts involving computer resources, including unauthorized access and copying/extraction of data."
        ],
        [
            "Section 66",
            "Addresses computer-related acts under Section 43 when performed dishonestly or fraudulently."
        ],
        [
            "Section 66C",
            "Addresses fraudulent or dishonest use of another person's electronic signature, password or other unique identification feature."
        ],
        [
            "Section 66D",
            "Addresses cheating by personation using a communication device or computer resource."
        ],
    ]
)

add_heading("9.2 Indian Criminal Law", 2)

add_paragraph(
    "The assignment requests IPC (1860) mapping. Historically, IPC Section "
    "420 addressed cheating and dishonest inducement to deliver property, "
    "while Section 419 addressed cheating by personation."
)

add_paragraph(
    "For current Indian criminal law, the Bharatiya Nyaya Sanhita, 2023 "
    "(BNS) is the relevant criminal code. Section 318 addresses cheating "
    "and Section 319 addresses cheating by personation."
)

add_heading("9.3 Electronic Evidence", 2)

add_paragraph(
    "The Bharatiya Sakshya Adhiniyam, 2023 contains provisions concerning "
    "electronic and digital records. Sections 61, 62 and 63 are relevant "
    "to the treatment and admissibility framework for electronic records."
)

add_heading("9.4 Budapest Convention", 2)

add_table(
    ["Provision", "Relevance"],
    [
        ["Article 7", "Computer-related forgery"],
        ["Article 8", "Computer-related fraud"],
        ["Article 16", "Expedited preservation of stored computer data"],
        ["Article 29", "Preservation and partial disclosure of traffic data"],
        ["Article 35", "24/7 network for immediate assistance"],
    ]
)

add_paragraph(
    "The Budapest Convention is particularly relevant to the simulated "
    "cross-border context because electronic evidence may require "
    "international preservation and cooperation."
)

# -------------------------------------------------
# CROSS-BORDER CHALLENGES
# -------------------------------------------------

add_heading("10. Cross-Border Investigation Challenges")

add_heading("10.1 Jurisdiction", 2)

add_paragraph(
    "Different jurisdictions may have different criminal laws, investigative "
    "powers, privacy requirements and evidence procedures."
)

add_heading("10.2 Volatile Electronic Evidence", 2)

add_paragraph(
    "Cloud-hosted logs, network information and other electronic evidence "
    "may be deleted or overwritten. Rapid preservation can therefore be "
    "important."
)

add_heading("10.3 International Cooperation", 2)

add_paragraph(
    "Investigators may need cooperation from foreign law-enforcement agencies, "
    "service providers or other competent authorities to obtain evidence "
    "located outside the investigating jurisdiction."
)

add_heading("10.4 Time Zones and Attribution", 2)

add_paragraph(
    "Different time zones and inconsistent timestamp formats can complicate "
    "timeline reconstruction. Investigators should document timezone "
    "assumptions and correlate multiple independent sources."
)

# -------------------------------------------------
# SOP RECOMMENDATIONS
# -------------------------------------------------

add_heading("11. Recommendations for Law-Enforcement SOPs")

recommendations = [
    "Standardize evidence identification and unique evidence IDs.",
    "Use validated acquisition procedures and write protection where appropriate.",
    "Calculate and record cryptographic hashes at acquisition.",
    "Maintain complete chain-of-custody records for every evidence transfer.",
    "Perform forensic analysis on verified copies whenever possible.",
    "Document search keywords, tools, versions and examination steps.",
    "Preserve volatile and remotely stored evidence as early as legally permitted.",
    "Maintain standardized timezone and timestamp documentation.",
    "Establish clear procedures for cross-border preservation and evidence requests.",
    "Provide recurring forensic training on emerging payment-card and online-fraud techniques.",
]

for i, recommendation in enumerate(recommendations, start=1):
    add_paragraph(f"{i}. {recommendation}")

# -------------------------------------------------
# LIMITATIONS
# -------------------------------------------------

add_heading("12. Investigation Limitations")

add_paragraph(
    "This project is a controlled academic simulation. The evidence files "
    "are synthetic and do not represent actual criminal evidence."
)

add_paragraph(
    "The simulated timestamps, transactions, communications, coordinates "
    "and identifiers are designed to demonstrate forensic methodology and "
    "should not be interpreted as evidence of a real-world offence."
)

# -------------------------------------------------
# CONCLUSION
# -------------------------------------------------

add_heading("13. Conclusion")

add_paragraph(
    "The Operation Phantom Swipe simulation demonstrates an end-to-end "
    "early-stage digital-forensics workflow. The investigation begins with "
    "crime classification and evidence preservation, followed by hashing, "
    "search, metadata examination, artefact extraction and controlled "
    "cryptography analysis."
)

add_paragraph(
    "The project also demonstrates why chain of custody, evidence integrity, "
    "lawful access and international cooperation are essential when digital "
    "evidence crosses organizational or national boundaries."
)

# -------------------------------------------------
# REFERENCES
# -------------------------------------------------

add_heading("14. References")

references = [
    "Information Technology Act, 2000 — India Code, Government of India.",
    "Bharatiya Nyaya Sanhita, 2023 — India Code, Government of India.",
    "Bharatiya Sakshya Adhiniyam, 2023 — India Code, Government of India.",
    "Convention on Cybercrime (Budapest Convention), Council of Europe.",
    "Assignment 1 – Unit 1: Foundations of Digital Forensics — Operation Phantom Swipe.",
]

for ref in references:
    add_paragraph(ref)

# -------------------------------------------------
# DECLARATION
# -------------------------------------------------

add_heading("15. Authorship Declaration")

add_paragraph(
    "I declare that the evidence dataset, forensic artefacts, analysis "
    "scripts and documentation included in this repository were prepared "
    "for academic purposes. All simulated evidence is synthetic."
)

add_paragraph(
    "The project does not contain real payment-card information, credentials "
    "or private data belonging to third parties."
)

# -------------------------------------------------
# SAVE
# -------------------------------------------------

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc.save(OUTPUT)

print("==============================================")
print("REPORT GENERATED SUCCESSFULLY")
print("==============================================")
print(f"File: {OUTPUT}")
