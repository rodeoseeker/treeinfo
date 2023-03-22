# treeinfo

This repository can be used to fetch images from Google using Google Custom Search API. It keeps the API usage under the Google's free-tier daily limit.

Usage:
1. Edit google_image_search.py to replace with your Google Custom Search API Key and Cx. Ask Chat-GPT on how to obtain these, if you don't know how.
2. You may edit the tree_info.html to udpate the tree list.
2. Run ./tree_info.py in a crontab once a day, until all tree data is updated.
3. run ./genhtml.py to generate an html page like https://rodeoseeker.github.io/tree_info.html


