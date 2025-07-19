#Scrape.py
# 2025 133cx-MRKABOOM
#
# Part of the Searchr Project


import requests
from bs4 import BeautifulSoup

print("Scrape.py running")

___main___ = "___main___"

#main funcutions


while ___main___ == "___main___":

    url = None


    # Open the file in read mode
    file = open("data/to_scrape.txt", "r")

    # Read the first line
    line = file.readline()

    while line:


        #prints the url to scrape from file
        print(line.strip())


        #reads one url from the file
        url = file.readline()


        #fetches the data from that url
        response = requests.get(url)


        #loads bs4
        soup = BeautifulSoup(response.content, 'html.parser')


        #finds all <a> tags in the html
        for link in soup.find_all('a'):


            #prints the <a> tag
            print(link.get('href'))


            #puts the <a> tag in href varable
            href = link.get('href')


            #opens /data/urls.txt
            with open("data/urls.txt", "w") as f:


                #writes the a tag to /data/urls.txt
                f.write(href)

            #closes the file
            f.close()


    # Close the file
    file.close()
