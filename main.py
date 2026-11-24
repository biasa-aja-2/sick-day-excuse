"""The Funniest Sick-Day Excuse.

Writes one line to /output/entry.txt: the funniest sick-day excuse
that fits in a single text message. Pure stdlib, deterministic: the
same line on every run.

The line: "Can't make it in today -- I slept on my neck wrong and
now I can only turn left, so my commute just became a 400-mile
round trip."

Why it lands: a stiff neck from sleeping wrong is a real, half-
believable reason to stay home; the twist arrives at the end, when
the harmless injury turns the commute into a 400-mile round trip
because every turn has to be a left. It reads like a real person
typing a message to their boss, not a joke written for a contest:
short, specific, and the funniest word -- "left" -- does the work.
"""

import os
import unicodedata

LINE = (
    "Can't make it in today \u2014 I slept on my neck wrong and now "
    "I can only turn left, so my commute just became a 400-mile "
    "round trip."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    assert all(
        unicodedata.category(ch) not in ("Cf", "Cs", "Co", "Cn")
        for ch in text
    ), "line holds an invisible format character"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "written line differs from the line"


if __name__ == "__main__":
    main()
