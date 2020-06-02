from bs4 import BeautifulSoup
import urllib.request
import re
import requests
from bs4.element import Comment


# method to store the text into the given file
def store_document(text, filename, url):
    with open(filename, 'w',encoding='utf-8') as f:
        f.writelines("URL : " + url + "\n")
        f.write(text)

        
        
# It validates the url for parsing         
def is_valid_extension(url):
        invalid_extensions = ["pdf", "jpg", "jpeg", "doc", "docx", "ppt", "pptx", "png", "txt", "exe", "ps", "psb"]
        if True in [ext in url for ext in invalid_extensions]:
            return False
        return True
        
# this fetchs the links from the html page content.        
def get_links(html_page):
    soup = BeautifulSoup(html_page,features="lxml")
    links = soup.findAll('a',href=True)
    return links

# This calls the url and fetchs the response as a string.
def get_html(url):
    try:
#         response = urllib.request.urlopen(url)
        response = requests.get(url)
#         if response.getcode()==200:
        return response.content.decode('latin-1')
#             return response.read()
    except Exception as e:
        print(e)
        return None
    
# This validates whether the tag is valid or not
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

# this gets the content from html page 
def get_text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

# it gives the links from page and save the content of website to a file
def get_links_and_save_content(url,filename):
    html_page = get_html(url)
    if html_page != None and 'Page Not Found' not in html_page:
        page_content = get_text_from_html(html_page)
        store_document(page_content,filename,url)
        return True, get_links(html_page)
    else:
        return False,[]
    