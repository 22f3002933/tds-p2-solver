import httpx
from bs4 import BeautifulSoup
import json

def get_imdb_movies():

    # Calculate r and n (rating range) using same logic as JavaScript
    r =3
    n =7
    while (n - r < 1):
        r = math.floor(random.random() * 7) + 2
        n = math.floor(random.random() * 7) + 2
        if r > n:
            r, n = n, r

    # Fetch IMDb data
    url = f"https://www.imdb.com/search/title/?user_rating={r},{n}"
    
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.imdb.com/",
        "Connection": "keep-alive"
    }

    with httpx.Client(timeout=30.0) as client:
        response = client.get(url, headers=headers, follow_redirects=True)

    soup = BeautifulSoup(response.text, 'html.parser')
    movies = []

    # Extract movie data using same selectors as JavaScript
    for item in soup.select(".ipc-metadata-list-summary-item"):
        movie_id = item.select_one(".ipc-title-link-wrapper")['href'].split('/')[2]
        title = item.select_one(".ipc-title__text").text
        year = item.select_one(".dli-title-metadata-item").text
        rating = item.select_one(".ipc-rating-star--rating").text
        
        movies.append({
            "id": movie_id,
            "title": title, 
            "year": year,
            "rating": rating
        })

    print(f"Movies with rating between {r} and {n}:")
    print(json.dumps(movies[:2], indent=2))

    return movies[:25]

# result = get_imdb_movies()
# print(f"Movies with rating between {result['r']} and {result['n']}:")
# print(json.dumps(result['movies'], indent=2))
