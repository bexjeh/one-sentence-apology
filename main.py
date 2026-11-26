import os

TEXT = "I'm sorry I reset your password to something so secure even I forgot it, so now neither of us can get into your own account."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
