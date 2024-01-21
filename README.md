# treeinfo

This repository can be used to fetch images from Google using Google Custom Search API. It keeps the API usage under the Google's free-tier daily limit.

Usage:
1. Edit google_image_search.py to replace with your Google Custom Search API Key and Cx. Ask Chat-GPT on how to obtain these, if you don't know how.
   Look for ...
      api_key = "<REPLACE WITH YOUR API-KEY>"
      cx = "<REPLACE WITH YOUR CX>"
2. You may edit the tree_info.py to udpate the tree list. You can not remove a tree from the list; only replace a tree with another tree.
   The pre-constructed ./tree_data will get messed up if you remove a tree without replacing it with another. The place of the trees that are not impacted in the list must not change.
   Note: To refresh a tree-data just remove the subdir under tree_data that matches the name in the namekey.txt. 
3. Run ./tree_info.py in a crontab once a day, until all tree data is updated.
4. run ./genhtml.py to generate an html page like https://rodeoseeker.github.io/tree_info.html


