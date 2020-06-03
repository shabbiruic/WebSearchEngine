# Web Search Engine

## Overview
In this Project I am building a web search
engine which will give the relevant top
50(default) website links depending on the
query and that will be ordered on the basis
of their relevance. For this started crawling
all the websites which are in uic domain and
collected around 3K website and its content.
After that we have generated the TF-IDF
vector out of the text contained in the
collected website. for finding the top most
relevant document we have fetched the
documents which has maximum similarity
with the query. For arranging the documents
in the order used the page rank algorithm
which gives the rank to page according to
its linkage with the other pages.

## Implementation Details
This project can be divided into the following
subtitles which are Web Crawler, Scrapper,
Document Vectorizer and Pagerank. So the
main task of a web Crawler is to collect the
website's links for processing. While a
Scrapper job is to scrap the useful
information out of this page like text
contains and links. Document Vectorizer will
convert the content associated with the URL
to the TF-IDF vector from which will later be
used to find its similarity with the provided
query. Page Rank performs the work of
assigning the rank to each page dependingon how it is linked to the other pages. We
will be needing this rank to sort the links
according to their importance.

## Various Module details in project
- **Web Crawling** : It is collecting the URL starting from the provided seed URL and fetch all its related pages and keep on doing it until desired amount of pages are collected. done by WebCrawler.ipynb
- **Web Scraping** : It is Parsing of the web Pages and collecting usual information from it like other pages link and data which is visible to user. It is done by Scrapper.py  
- **Vectorizing** : We are calculating the **TF-IDF** from the fetched web pages data so as to convert their content into the vector form which later can be used for calculation of similarity of query. It is done by Vectorizer.iynpb.
- **Ranking** : We are providing the rank to each web pages depending on its links to various pages and their ranks. So we have used **Page Rank Algorithm** to rank them. It is done by PageRank.ipynb
- **Search** : One of the main task is to get the relevant links depending on query. For this first we calculates the Vector form of query in the similar way which is done for all the web pages content then computes **cosine similarity** of query vector with all the web pages and gives the top most similar web pages URL. After that sort those URLs depending on the ranks which is calculated in above step and sort it. These all stepa are done by Searh.py
- **User Interface** : This is place throw which user interact with the system. Here he can provide the textbox where query can be entered and search. User can also navigate to and fro across the fetched URLs with provided buttons. this is done by UI.iynpb.
- **Configuration** : This is file where all the project related configuration are present which user has to mandatorily set if he/she wants to run the project in expected way. it is store in file Configuration.py
description about how to set these parameters is provided in the file itself.

## Perquisite for running the project
- jupyter notebook or you can run it in Google colabs any one is sufficient.
- Following libraries should be installed.
  1. Pandas
  2. Pickle
  3. BeautifulSoup
  4. numpy
  5. sklearn
  6. Vectorizer
  7. NLTK
  
## Steps to Run the Project
1.	Download the provide zip folder and extract it.
2.	It has already pre-calculated TF-IDF, vectorizer and Page Rank that can be used.
3.	If you are using the pre computed then just open the jupyter note book and run the file name UI.ipynb it will open the UI window like this
 ![Screen Shot of Seatch Engine UI](https://github.com/shabbiruic/WebSearchEngine/blob/master/ScreenShot.png)
4. If you want to compute everything from scratch then follow this steps it will take around 1:30 to 2 hours computation time.
  - First run the WebCrawler.ipynb file by just opening it and running its first cell in juypter notebook
  - Then run the Vectorier.ipynb file by just opening it and running its first cell in juypter notebook.
  - After then run the PageRank. ipynb file by just opening it and running its first cell in juypter notebook.
  - Now at last run the UI.ipynb file by just opening it and running its first cell in juypter notebook. it Will open the GUI whose image is described above.





