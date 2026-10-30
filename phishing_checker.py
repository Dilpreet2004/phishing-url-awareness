import re
from urllib.parse import urlparse

# Commonly abused top-level domains frequently used in phishing campaigns
SUSPICIOUS_TLDS = {".zip", ".mov", ".top", ".xyz", ".tk", ".ga", ".cf", ".gq", ".ml"}

# Keywords frequently targeted in path/query parameters to trick users
SUSPICIOUS_KEYWORDS = ["login", "verify", "bank", "secure", "update", "paypal", "account", "signin"]

def inspect_url(raw_url):
  """Check visible URL text for selected warning signs."""
  url = raw_url.strip()
  findings = []

  if not url:
    return ["No URL entered."]

  candidate = url if "://" in url else "http://" + url
  parsed = urlparse(candidate)
  host = (parsed.hostname or "").lower()

  if not host:
    return ["Could not identify a hostname."]

  if "@" in candidate:
    findings.append("Contains an @ symbol; inspect carefully.")

  if len(url) > 100:
    findings.append("Unusually long URL (over 100 characters).")

  if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
    findings.append("Uses an IP address instead of a familiar domain.")

  labels = [part for part in host.split(".") if part]
  if len(labels) >= 5:
    findings.append("Contains many hostname segments/subdomains.")

  if "xn--" in host:
    findings.append("Contains a punycode-style hostname.")

  if parsed.scheme.lower() == "http":
    findings.append("Uses HTTP, HTTPS alone does not prove trust.")

  # Improvement 1: Check for high-risk TLDs
  if any(host.endswith(tld) for tld in SUSPICIOUS_TLDS):
    findings.append("Uses a high-risk top-level domain commonly associated with phishing.")

  # Improvement 2: Check for sensitive keywords outside of domain
  path_and_query = (parsed.path + parsed.query).lower()
  detected_keywords = [kw for kw in SUSPICIOUS_KEYWORDS if kw in path_and_query]
  if detected_keywords:
    findings.append(f"Contains sensitive target keywords in path/query: {', '.join(detected_keywords)}.")

  if not findings:
    findings.append("No listed warning signs found. This does NOT prove safety.")

  return findings

def main():
  print("EWB phishing URL Awareness Checker")
  print("Texts checks only - this program does not open URLs.")
  raw_url = input("Enter a sample URL to inspect: ")
  print("\nResults:")
  for item in inspect_url(raw_url):
    print("- " + item)
  print("\nNever enter passwords from unexpected links.")

if __name__ == "__main__":
  main()