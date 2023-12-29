import requests
from bs4 import BeautifulSoup

def extract_and_save_html(url, output_file='website_source_code.html'):
    try:
        # Fetch the web page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad requests

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Prettify the HTML content (optional, for better readability)
        prettified_html = soup.prettify()

        # Save the HTML content to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(prettified_html)

        print(f"Source code extracted and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the web page: {e}")

if __name__ == "__main__":
    # Specify the URL of the website you want to extract
    website_url = 'https://software.techkeshri.com'

    # Call the function to extract and save the HTML content
    extract_and_save_html(website_url)
