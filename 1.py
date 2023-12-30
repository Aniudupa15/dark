import requests
from bs4 import BeautifulSoup

def has_hidden_links(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all links (a tags) in the HTML
        links = soup.find_all('a')

        # Check for hidden links
        hidden_links = [link for link in links if link.get('style') and 'display:none' in link.get('style').lower()]

        if hidden_links:
            return True, hidden_links
        else:
            return False, None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False, None

# Example usage
url = 'https://www.amazon.in'
is_dark_pattern, hidden_links = has_hidden_links(url)

if is_dark_pattern:
    print("Dark Pattern Detected: Hidden Links")
    for link in hidden_links:
        print(f"Hidden Link: {link.get('href')}")
else:
    print("No dark patterns detected.")
