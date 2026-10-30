# EWB Phishing URL Awareness Checker

## Overview

Phishing is a social engineering attack where malicious actors use deceptive links to trick users into revealing sensitive information. This tool analyzes raw URL strings to highlight common technical warning signs without visiting or initiating network requests to the target links.

## Features

- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- Flags high-risk top-level domains (TLDs) frequently abused in phishing attacks
- Flags sensitive target keywords (e.g., `login`, `verify`, `account`) found in the path or query string

## Requirements

Python 3.10 or later. No extra packages required.

## How to Run

Windows:
```
python phishing_checker.py
```

Mac/Linux:
```
python3 phishing_checker.py
```

## Example Output

```
EWB phishing URL Awareness Checker
Texts checks only - this program does not open URLs.
Enter a sample URL to inspect: http://login.verify-account.top/login?user=test

Results:
- Uses HTTP, HTTPS alone does not prove trust.
- Uses a high-risk top-level domain commonly associated with phishing.
- Contains sensitive target keywords in path/query: login.

Never enter passwords from unexpected links.
```

## Testing

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | `https://www.example.com/login` | Flags sensitive keywords | Contains sensitive target keywords in path/query: login. | Pass |
| 2 | `http://192.0.2.10/account` | IP address + HTTP + Keywords | Uses an IP address instead of a familiar domain. / Uses HTTP, HTTPS alone does not prove trust. / Contains sensitive target keywords in path/query: account. | Pass |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP + Keywords | Contains an @ symbol; inspect carefully. / Uses HTTP, HTTPS alone does not prove trust. / Contains sensitive target keywords in path/query: login. | Pass |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. | Pass |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. | Pass |
| 6 | `https://my-free-download.zip/setup` | High-risk TLD warning | Uses a high-risk top-level domain commonly associated with phishing. | Pass |
| 7 | `https://www.legitimate-domain.com/login/secure/verify-account` | Keywords in path/query | Contains sensitive target keywords in path/query: login, secure, verify, account. | Pass |

## Screenshots

![Sample run](screenshots/sample_run.png)
![Test results](screenshots/test_results.png)

## Improvements

1. **High-Risk TLD Detection** - Added a check for top-level domains (e.g., `.top`, `.xyz`, `.zip`) frequently abused for phishing. Tested by supplying hostnames ending in these TLDs and verifying warning flags are generated.
2. **Sensitive Keyword Inspection** - Added inspection of the URL path and query string for sensitive credentials/banking keywords (e.g., `login`, `verify`, `account`). Tested using URLs with path/query parameters containing target strings.

## Limitations

This is an educational tool. It only reads URL text. It does not visit URLs, scan for malware, or prove that a URL is safe. No warning signs found does NOT mean a URL is safe.

## Ethical Use

Use sample strings only. Do not collect credentials. Do not use this project to deceive anyone or to test websites without permission.

## Author

Dilpreet Singh, AI powered Cybersecurity INTERNSHIP, EWB Courses