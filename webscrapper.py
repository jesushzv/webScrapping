# Import the relevant libraries
import requests
from bs4 import BeautifulSoup

# Function that will do the actual web scrapping


def scrape():

    # URL of the web page
    url = "https://latinus.us/2021/03/28/decomisan-aicm-44-mil-kits-pruebas-covid-pretendian-ingresadas-forma-ilegal/"

    # Retrieve content of url
    content = requests.get(url)

    # Parse html content
    content = BeautifulSoup(content.content, 'html.parser')

    # Return the text in all the p tags of the parsed html content in a list
    return [p.text for p in content.find_all('p')]

# Function to create text file


def textfile():
    # Return the text in all the p tags of the parsed html content in a list
    story = scrape()

    # Creates and opens a text file to write in
    newsFile = open('article.txt', 'w')

    # Iterate the story and write a line in the newsFile for every member of the list
    for i in story:
        newsFile.write(i)
        newsFile.write('\n')

    # Close txt file
    newsFile.close()

    # Sucess msg
    print('Success!')

textfile()
