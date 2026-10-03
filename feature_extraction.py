import re
from urllib.parse import urlparse
import tldextract

def extract_features(url):
    features = {}
    
    # 1. URL Length
    features['url_length'] = len(str(url))
    
    # 2. Count specific character patterns commonly used by attackers
    features['qty_dots'] = str(url).count('.')
    features['qty_hyphens'] = str(url).count('-')
    features['qty_at'] = str(url).count('@')
    features['qty_question'] = str(url).count('?')
    features['qty_equal'] = str(url).count('=')
    
    # 3. Check for HTTPS usage (0 = HTTPS, 1 = HTTP)
    features['is_http'] = 1 if str(url).startswith('http://') else 0
    
    # 4. Check if the domain name is a direct, numeric IP address
    ip_pattern = r'^(http|https)://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    features['is_ip'] = 1 if re.match(ip_pattern, str(url)) else 0
    
    # 5. Extract subdomains using tldextract library
    extracted = tldextract.extract(str(url))
    subdomain = extracted.subdomain
    features['qty_subdomains'] = len(subdomain.split('.')) if subdomain else 0
    
    # 6. Check for suspicious standard phishing keywords
    keywords = ['login', 'verify', 'secure', 'bank', 'update', 'account', 'signin']
    features['has_suspicious_keyword'] = 1 if any(kw in str(url).lower() for kw in keywords) else 0
    
    return features

# Quick test module to run in your console
if __name__ == "__main__":
    test_url = "http://secure-bank-verify.com"
    print("Testing Feature Extraction on:", test_url)
    print(extract_features(test_url))
