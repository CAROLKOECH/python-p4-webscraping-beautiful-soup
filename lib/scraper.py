# scraper.py
from bs4 import BeautifulSoup
import requests

# Set the user-agent header to avoid being blocked by some websites
headers = {'user-agent': 'my-app/0.0.1'}

# Send an HTTP GET request to the website
url = "https://flatironschool.com/"
html = requests.get(url, headers=headers)

# Parse the HTML content using Beautiful Soup
doc = BeautifulSoup(html.text, 'html.parser')

# Example 1: Extract and print the content of an element with class 'heading-financier'
heading = doc.select('.heading-financier')
if heading:
    heading_text = heading[0].contents[0].strip()
    print(heading_text)

# Example 2: Extract and print the titles of all elements with specific classes
courses = doc.select('.heading-60-black.color-black.mb-20')
for course in courses:
    course_title = course.contents[0].strip()
    print(course_title)

# Example 3: Accessing element attributes (e.g., class)
first_course = doc.select('.heading-60-black.color-black.mb-20')
if first_course:
    class_name = first_course[0]['class']  # Get the list of classes
    print(class_name)

# Example 4: Accessing child elements
div_with_h2 = doc.select('.example-div')
if div_with_h2:
    child_h2 = div_with_h2[0].find('h2')  # Find the first 'h2' element within the div
    if child_h2:
        child_text = child_h2.contents[0].strip()
        print(child_text)
