#!/usr/bin/env python3
"""
Sample application using vulnerable dependencies from VDR report.
Used for testing OSV.dev fallback for fix version resolution.
"""

import sys
from pathlib import Path

# Use filelock
try:
    from filelock import FileLock
    lock = FileLock("/tmp/vdr_test.lock")
    print(f"FileLock version: {FileLock.__module__}")
except ImportError:
    print("filelock not installed")

# Use setuptools
try:
    import setuptools
    print(f"setuptools version: {setuptools.__version__}")
except ImportError:
    print("setuptools not installed")

# Use wheel
try:
    import wheel
    print(f"wheel version: {wheel.__version__}")
except ImportError:
    print("wheel not installed")

# Use requests
try:
    import requests
    print(f"requests version: {requests.__version__}")
except ImportError:
    print("requests not installed")


def main():
    print("=" * 50)
    print("VDR Python Test Application")
    print("=" * 50)
    print(f"Python version: {sys.version}")
    print(f"Working directory: {Path.cwd()}")
    print("=" * 50)
    print("Application completed successfully!")


if __name__ == "__main__":
    main()
