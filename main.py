"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os

ENTRY = "My AI wrote my dating profile, and now even the chatbots are ghosting me."


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be blank"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    try:
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        path = "./output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)

    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip check failed"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"written to: {path}")


if __name__ == "__main__":
    main()
