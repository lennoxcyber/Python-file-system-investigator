# Python File System Investigator

A beginner cybersecurity project built with Python.

## Features

- Recursively scans directories and subdirectories
- Identifies files with selected potentially risky extensions
- Records file paths and sizes
- Calculates SHA-256 file hashes
- Exports scan results to a CSV report
- Handles file-access and hashing errors

## Requirements

- Python 3
- No third-party packages required

## How to Run

1. Open a terminal in the project directory.
2. Run `python main.py`.
3. Enter the directory path you want to scan.
4. Open `scan_report.csv` to review the results.

## Limitations

Flagged file extensions do not prove a file is malicious.
SHA-256 hashes identify file contents but do not determine
whether a file is safe.
