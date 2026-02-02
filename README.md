# VDR Python Test

Test repository for testing OSV.dev fallback for fix version resolution in Backline.

## Vulnerable Packages

This project includes dependencies with known vulnerabilities from VDR reports:

| Package | Version | Vulnerability | Trivy Fix | OSV Fallback |
|---------|---------|---------------|-----------|--------------|
| filelock | 3.19.1 | GHSA-w853-jp5j-5j7f | Yes | N/A |
| pip | 20.3.4 | GHSA-5xp3-jfq3-5q8x, GHSA-mq26-g339-26xf | Yes | N/A |
| setuptools | 44.1.1 | CVE-2022-40897, CVE-2025-47273, GHSA-r9hx-vwmv-q579 | Yes | N/A |
| wheel | 0.34.2 | GHSA-qwmp-2cf2-g9g6 | Yes | N/A |
| requests | 2.25.0 | CVE-2023-32681 | Yes | N/A |
| urllib3 | 1.26.5 | CVE-2021-33503 | Yes | N/A |
| dspy | 2.5.0 | CVE-2025-12695 | No | No fix available |
| **scrapy** | **2.11.0** | **GHSA-23j4-mw76-5v7h** | **No** | **Yes → 2.11.2** |

**OSV Fallback Test Cases**:
- `scrapy@2.11.0` - **TRUE POSITIVE**: Trivy has no fix, OSV returns fix version `2.11.2`
- `dspy@2.5.0` - Triggers OSV fallback but neither Trivy nor OSV have a fix available

## Usage

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Testing with Backline

1. Upload `vdr-report.csv` as Custom Report
2. Use `vdr-csv-mapping.yaml` as config file
3. Repository URL: https://github.com/backline-playground/vdr-python-test
