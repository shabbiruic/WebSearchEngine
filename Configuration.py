# this is the file where all the configuration of projects are stored. i.e. path to various folder and name of file which will get generated 
# after running the project.

# This all paths are relative with assumption that where ever you are running this project it structure will be same as downloaded from provide zip. If you change the structure you have to change the path accordingly.

# name of file where data frame is stored during vectorizing the web page contains
path_data_frame = 'DataFrame3000'

# name of vectorizer file where it will be stored.
path_to_vectorizer = 'Vectorizer3000'

# this name where tfidf of all the pages will be stored
path_to_document_tfidf = 'DocumentTFIDF3000'

# this is the name of folder where the all parsed url contents are placed.
path_to_document_folder = 'WebContent3000'

# file name where WebGraph is stored during web crawling.
path_to_web_graph = 'WebGraph3000'

# Here page rank values for all the crawled web pages will be stored
path_to_page_rank = 'PageRank3000'

# value of alpha used during page rank calculation.
alpha = .15

# maximun number of iteration to be done for page rank calculation.
number_of_iteration_in_rank = 300