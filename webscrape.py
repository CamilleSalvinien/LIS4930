#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# libraries needed
import requests
import urllib.request
from urllib.request import urlopen
import time
from bs4 import BeautifulSoup
print("Done")


# In[56]:


# web page we will be scraping
url = "https://camillesalvinien.wixsite.com/bloglis4930-1"
# read it with url open
page = urlopen(url)
print(page)


# In[ ]:


# reading it as an html page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)


# In[58]:


# finding the title of the web page
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(title)


# In[ ]:


# web scraping using beautifulsoup
url = 'https://camillesalvinien.wixsite.com/bloglis4930-1/post/data-visualization'
response = requests.get(url)
page = BeautifulSoup(response.text)
print(page.prettify())


# In[60]:


# title
page.title.string


# In[ ]:


# test
page.get_text()


# In[54]:


# paragraph class
page.p

