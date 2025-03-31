import httpx
from bs4 import BeautifulSoup
from urllib.parse import urlencode

def get_hackernews_link():
    # Construct the HNRSS URL with parameters
    params = {
        'q': "Saas",
        'points': 83
    }
    url = f"https://hnrss.org/newest?{urlencode(params)}"

    # Fetch and parse the RSS feed
    with httpx.Client(timeout=30.0) as client:
        response = client.get(url)

    response.raise_for_status()  # Check for errors
    
    # Parse XML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first item's link
    first_link = soup.find('item')
    if not first_link:
        raise Exception("No items found")
    
    link = first_link.find('guid').text
    print(f"Link: {link}")

    return link 

# try:
#     link = get_hackernews_link()
#     print(link)
# except Exception as e:
#     print(f"Error: {e}")