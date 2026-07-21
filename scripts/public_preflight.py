#!/usr/bin/env python3
"""Fail fast when a public Git commit appears to cross the privacy boundary."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_PATH_PARTS = {
    "_lessons_docs",
    "PROJECT_BRAIN/PRIVATE",
    "_private",
    "ethics",
    "supervision",
    "participant_data",
    "consent",
    "data/raw",
    "data/private",
    "data/restricted",
    "reports/drafts",
    "reports/submission",
    "references",
    "secrets",
}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "generic secret assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}['\"]"
    ),
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".ipynb",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".csv",
    ".tsv",
    ".html",
    ".css",
    ".js",
    ".ts",
    ".sh",
}


def tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def main() -> int:
    problems: list[str] = []

    try:
        files = tracked_files()
    except subprocess.CalledProcessError:
        print("ERROR: run this check inside the initialised public Git repository.")
        return 2

    for relative in files:
        normalised = relative.replace("\\", "/")
        lowered = normalised.lower()

        for part in FORBIDDEN_PATH_PARTS:
            if part.lower() in lowered:
                problems.append(f"forbidden tracked path: {relative}")

        path = ROOT / relative
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            problems.append(f"unreadable text file: {relative}")
            continue

        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                problems.append(f"possible {label} in: {relative}")

    if problems:
        print("PUBLIC PREFLIGHT FAILED")
        for problem in sorted(set(problems)):
            print(f"- {problem}")
        return 1

    print(f"PUBLIC PREFLIGHT PASSED: {len(files)} tracked files checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
