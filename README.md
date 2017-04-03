# Dummy_Search
This Search Engine is Designed to Search News Specifically
To Start open the spiderVer32.py to generate Spider
Name the number of Spider and number of iterartions after which it should stop.
The Reason is that The Web is an infinite collection of data and we would like to stop after some time to continue our analysis
Then Open the link-outlink.py to generate which web page points to where 
This will help in the Calculation of Page-Rank which is the main ranking mechanism behind the Search Engine
Next Calculate the Page Rank by running SetupPageRank.m
When it is done upload the data in a a sqllite database by running the latest version of create-databse.py
Now Run the query module to see the relevant results appear in the dexcreasing order of page rank
