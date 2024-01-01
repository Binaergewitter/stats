# Helper script to create a CSV from rss feed
# pip install feedparser
import feedparser

url = "https://blog.binaergewitter.de/podcast_feed/all/mp3/rss.xml"

PodcastFeed = feedparser.parse(url)

print("Name,Date,Type,Duration,ingo,l33tname,madmas,makefu,pfleidi,marc")
for e in PodcastFeed.entries:
    if e.published_parsed.tm_year == 2023:
      date_str = f"{e.published_parsed.tm_mday}.{e.published_parsed.tm_mon}.{e.published_parsed.tm_year}" 
      ingo = int("ingo" in e.podcast_person)
      l33tname = int("l33tname" in e.podcast_person)
      madmas = int("madmas" in e.podcast_person)
      makefu = int("makefu" in e.podcast_person)
      print(f"\"{e.title}\",{date_str},Talk,{e.itunes_duration},{ingo},{l33tname},{madmas},{makefu},0,0")

