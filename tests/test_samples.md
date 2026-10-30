# Test Results 
Python version used: 3.13.2   |   Operating system: Windows 11   |   Date: 30-October-2026 

| # | Input | Expected result | Actual result | Pass/Fail |
|---|-------|-----------------|---------------|-----------|
| 1 | `https://www.example.com/login` | Flags sensitive keywords | Contains sensitive target keywords in path/query: login. | Pass |
| 2 | `http://192.0.2.10/account` | IP address + HTTP + Keywords | Uses an IP address instead of a familiar domain. / Uses HTTP, HTTPS alone does not prove trust. / Contains sensitive target keywords in path/query: account. | Pass |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP + Keywords | Contains an @ symbol; inspect carefully. / Uses HTTP, HTTPS alone does not prove trust. / Contains sensitive target keywords in path/query: login. | Pass |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. | Pass |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. | Pass |
| 6 | `https://my-free-download.zip/setup` | High-risk TLD warning | Uses a high-risk top-level domain commonly associated with phishing. | Pass |
| 7 | `https://www.legitimate-domain.com/login/secure/verify-account` | Keywords in path/query | Contains sensitive target keywords in path/query: login, secure, verify, account. | Pass |
# Notes
Building and testing this script highlighted how simple URL parsing logic can effectively catch common phishing indicators like IP obfuscation, punycode, and embedded credentials. It was surprising how easily basic string and standard library checks (urllib.parse) can reveal deceptive structures without needing external dependencies or network traffic.