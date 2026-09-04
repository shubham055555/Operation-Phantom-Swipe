# Operation Phantom Swipe
## Cryptography Investigation Notes

### Objective

A password-protected evidence container was simulated
as part of the digital-forensics investigation.

The protected container contains synthetic academic
evidence only.

### Protected Evidence

Evidence container:
`crypto/phantom_protected.zip`

Protected files:

- confidential_note.txt
- transaction_batch.txt

### Password Testing Method

A controlled dictionary approach was simulated against
the synthetic password created for this assignment.

Dictionary file:

`crypto/password_dictionary.txt`

Synthetic password:

`Phantom2026!`

### Result

The simulated dictionary search located the synthetic
password after 7 candidate attempts.

This demonstrates how a dictionary-based password
testing approach can identify weak, predictable
passwords when the correct candidate exists in the
dictionary.

### Ethical and Legal Considerations

Password cracking should only be performed with
appropriate authorization and for a legitimate
forensic purpose.

Unauthorized attempts to access protected information
may violate applicable law and privacy/security
requirements.

In a real forensic investigation, investigators should
follow applicable legal procedures and obtain the
required authority before attempting to access
protected evidence.

### Password Strength Reflection

Common and predictable passwords are more susceptible
to dictionary-based attacks.

Longer and less predictable passwords increase the
number of possible candidates and generally make
guessing more difficult.

The password in this assignment was intentionally
created as synthetic training data so that the
investigation workflow could be demonstrated.

### Investigation Limitation

This project does not target any real account, device,
password or computer system.

All evidence, passwords, transactions and identifiers
are synthetic and were created exclusively for this
academic digital-forensics assignment.
