import requests
from bs4 import BeautifulSoup

url = "https://shop.royalchallengers.com/ticket"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all buttons with class chakra-button and type button
    buttons = soup.find_all('button', {'class': 'chakra-button', 'type': 'button'})
    
    # Check if any of the buttons have text "BUY TICKETS"
    for button in buttons:
        if button.text.strip() == "BUY TICKETS":
            print("Button with text 'BUY TICKETS' found.")
            # Log the button if needed
else:
    print("Failed to retrieve the webpage")
