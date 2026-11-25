"""The Funniest Toaster Error Message.

Writes one deadpan toaster error message to /output/entry.txt.
The joke: a real HTTP-style error code (451, unavailable for legal
reasons) applied to toast, with the bread lawyering up.
"""

from pathlib import Path

MESSAGE = "ERROR 451: Your toast is unavailable for legal reasons. The bread has a lawyer."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
