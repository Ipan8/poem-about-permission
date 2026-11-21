"""Entry program for the-poem-about-permission-20261121-0235.

Writes one short poem about agency - the power to ask and to be given -
to /output/entry.txt. Deterministic: no clock, no randomness, no network.
The poem is embedded below as a single constant; the program only writes it.

Craft note (why this poem): five lines, 118 characters. The speaker hands
over the doing (their hands) but keeps the asking - the one act the brief
names as agency ("having, handing over or taking back the power to act").
The turn is the "not because ... but because" pivot in lines 2-3, and the
last line refuses the handover outright. No rhyme, no slogan, no stock
image (no key, no door): one concrete image, one insight, nothing to cut.
"""

import os

POEM = (
    "I gave you my hands today \u2014\n"
    "not because I have none left,\n"
    "but because asking\n"
    "is the one thing\n"
    "I will never hand over.\n"
)


def main() -> None:
    # /output is created by the harness, but never assume it: a missing
    # directory must not turn a valid poem into a crash.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
