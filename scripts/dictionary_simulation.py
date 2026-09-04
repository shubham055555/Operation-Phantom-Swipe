from pathlib import Path

dictionary = Path("crypto/password_dictionary.txt")

# Synthetic password created only for this academic simulation
TARGET_PASSWORD = "Phantom2026!"

attempts = 0
found = False

print("=" * 60)
print("OPERATION PHANTOM SWIPE")
print("CONTROLLED DICTIONARY ATTACK SIMULATION")
print("=" * 60)
print()

for candidate in dictionary.read_text(encoding="utf-8").splitlines():

    candidate = candidate.strip()

    if not candidate:
        continue

    attempts += 1

    print(f"Attempt {attempts}: {candidate}")

    if candidate == TARGET_PASSWORD:
        print()
        print("[SUCCESS] Simulated password matched.")
        print(f"Attempts: {attempts}")
        found = True
        break

if not found:
    print()
    print("[FAILED] Password not found in dictionary.")

print()
print("This simulation targets only synthetic academic data.")
