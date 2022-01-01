# Helper script to create a CSV from rss feed
# pip install feedparser
import feedparser

url = "https://blog.binaergewitter.de/podcast_feed/all/mp3/rss.xml"

PodcastFeed = feedparser.parse(url)

print("Name,Date,Type,Duration,ingo,l33tname,madmas,makefu,pfleidi,marc")
for e in PodcastFeed.entries:
    if e.published_parsed.tm_year == 2021:
      date_str = f"{e.published_parsed.tm_mday}.{e.published_parsed.tm_mon}.{e.published_parsed.tm_year}" 
      print(f"\"{e.title}\",{date_str},Talk,{e.itunes_duration},0,0,0,0,0,0")

