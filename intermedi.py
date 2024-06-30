import re
from bs4 import BeautifulSoup
import requests

def extract_code_from_html(url):
    # Fetch HTML content
    response = requests.get(url)
    html_content = response.text
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract JavaScript code from <script> tags
    scripts = soup.find_all('script')
    js_code = [script.get_text() for script in scripts]
    
    return js_code

def analyze_js_code(js_code):
    api_patterns = {
        'oauth_token': r'Bearer\s+[A-Za-z0-9-_]+',
        'api_key': r'API_KEY\s*=\s*[\'"][A-Za-z0-9-_]+[\'"]',
        'credentials': r'(username|email)\s*:\s*[\'"][^\'"]+[\'"],\s*(password)\s*:\s*[\'"][^\'"]+[\'"]'
    }
    
    results = []
    
    for index, code_block in enumerate(js_code):
        for key, pattern in api_patterns.items():
            matches = re.finditer(pattern, code_block, re.IGNORECASE)
            for match in matches:
                results.append({
                    'type': key,
                    'value': match.group(),
                    'location': f'JavaScript block {index + 1}',
                    'position': match.span()
                })
    
    return results

# Example usage:
url = 'https://example.com'
js_code = extract_code_from_html(url)
leaks = analyze_js_code(js_code)

for leak in leaks:
    print(f"Found {leak['type']} leak: {leak['value']} at {leak['location']} (position {leak['position']})")
