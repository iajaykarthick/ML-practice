import os
from bs4 import BeautifulSoup

# The directory containing the HTML files
directory = os.getcwd()
directory = os.path.join(directory, 'docs')

# The name of the index file
index_file = 'index.html'

# Read the existing index.html content
with open(os.path.join(directory, index_file), 'r', encoding='utf-8') as file:
    index_html = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(index_html, 'html.parser')

# Find the <ul> element where we will add the links
ul = soup.find('ul')

# Clear existing <li> elements
ul.clear()

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Check if the current file is an HTML file and not the index file
    if filename.endswith('.html') and filename != index_file:
        # Create a new <li> element
        new_li = soup.new_tag('li')
        # Create a new <a> element
        new_link = soup.new_tag('a', href=filename)
        # Set the link text to the filename (without the .html extension)
        new_link.string = filename.replace('.html', '')
        # Add the link to the list item
        new_li.append(new_link)
        # Add the list item to the <ul> element
        ul.append(new_li)

# Write the updated HTML back to the index file
with open(os.path.join(directory, index_file), 'w', encoding='utf-8') as file:
    file.write(str(soup.prettify()))
