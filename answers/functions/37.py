from bs4 import BeautifulSoup
import httpx

def get_cricket_stats_answer():

    page_number = 7
    # Create URL
    url = f"https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;page={page_number};template=results;type=batting"

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Cache-Control": "max-age=0"
        }

    with httpx.Client() as client:
        response = client.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize sum
    total_ducks = 0

    # Find tables in the page
    for table in soup.find_all('table'):
        # Look for table with 50+ rows (main stats table)
        if len(table.find_all('tr')) >= 50:
            # Get headers
            headers = [th.text.strip() for th in table.find('thead').find_all('th')]
            
            # Process each row
            for row in table.find('tbody').find_all('tr'):
                cells = [td.text.strip() for td in row.find_all('td')]
                row_data = dict(zip(headers, cells))
                
                # Sum up the "0" column values
                total_ducks += int(row_data.get('0', 0))
    
    print(f"Total ducks in page {page_number}: {total_ducks}")

    return total_ducks


# Call the function and print the result with await
# get_cricket_stats_answer()
