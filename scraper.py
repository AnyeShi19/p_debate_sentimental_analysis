import snscrape.modules.twitter as st
import datetime
import json

# snscrape --jsonl twitter-search 'election2020 since:2020-10-01 until:2020-11-20' > search_results.json
# snscrape --jsonl --max-results 250 twitter-hashtag donaldtrump > ee2.json  

##################
# User configurations
queries = ["trump", "biden"]
hashtags = ["donaldtrump"]
max_tweets = 150
start_date = "2020-04-21"
end_date = "2020-04-21"
search_filename = "search_results"
hashtag_filename = "hashtag_results"
##################

start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
end = datetime.datetime.strptime(end_date, "%Y-%m-%d")

for query in queries:
    f = open(search_filename + "_" + query + ".txt", "a")
    query_with_criterion = query + "since:" + str(start) + " " + "until:" + str(end)
    search_results = st.TwitterSearchScraper(query=query_with_criterion).get_items()
    for cnt, search_result in enumerate(search_results):
        j = json.loads(search_result.json())
        # j.keys()  ## Search for possible keys
        f.write(j["content"])
        if cnt == max_tweets:
            break
    f.close()


for tag in hashtags:
    f = open(hashtag_filename + "_" + tag + ".txt", "a")
    hashtag_result = st.TwitterHashtagScraper(hashtag=tag)
    for cnt, search_result in enumerate(hashtag_result):
        j = json.loads(hashtag_result.json())
        f.write(j["content"])
        if cnt == max_tweets:
            break
    f.close()
