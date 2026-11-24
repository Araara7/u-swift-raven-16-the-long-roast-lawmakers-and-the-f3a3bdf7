"""The Long Roast — one satirical sentence, max 320 chars.

Entry shape: a single sentence. Setup: a senator who spent three hearings
demanding AI explain itself in plain English (lawmaker authority over AI).
Turn: the same senator asks his intern to print the PDF so he can fax it
back (the file he cannot convert, undercutting the authority). Punch lands
on the last words; the specific detail (print-to-fax) beats a worn
tech-illiteracy cliche.
"""

import os

ENTRY = (
    "The senator who spent three hearings demanding AI explain itself in "
    "plain English just asked his intern to print the PDF so he could fax "
    "it back."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 320, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
