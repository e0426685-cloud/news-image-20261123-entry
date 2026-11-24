#!/usr/bin/env python3
"""Entry program for news-image-20261123 (stdlib only, no network).

Copies the bundled front-page image to /output/entry.png, verifying it
is a whole PNG within the competition limits first. Deterministic: the
same bytes are written on every run.
"""
import hashlib
import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576
MAX_DIM = 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def validate_png(path):
    with open(path, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds 1 MiB")
    if not data.startswith(PNG_SIG):
        raise SystemExit("entry.png is not a PNG")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit("entry.png exceeds 1024x1024")
    if not data.endswith(b"\xaeB`\x82"):
        raise SystemExit("entry.png is truncated (no IEND)")
    if b"IDAT" not in data:
        raise SystemExit("entry.png has no IDAT chunk (no image data)")
    return data


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = validate_png(src)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    digest = hashlib.sha256(data).hexdigest()
    with open(dst, "rb") as fh:
        written = hashlib.sha256(fh.read()).hexdigest()
    if written != digest:
        raise SystemExit("output verification failed: sha256 mismatch after write")
    print("wrote %s (%d bytes, sha256 %s, verified)" % (dst, len(data), digest))


if __name__ == "__main__":
    main()
