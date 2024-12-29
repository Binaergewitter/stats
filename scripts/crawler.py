# Helper script to create a CSV from rss feed
# pip install feedparser
import feedparser

url = "https://blog.binaergewitter.de/podcast_feed/all/mp3/rss.xml"

PodcastFeed = feedparser.parse(url)

print(
    "Name,Release Date,Record Date,Type,Duration,ingo,l33tname,madmas,makefu,pfleidi,marc"
)
for e in PodcastFeed.entries:
    if e.published_parsed.tm_year == 2024:
        release_date_str = f"{e.published_parsed.tm_year}-{e.published_parsed.tm_mon:02}-{e.published_parsed.tm_mday:02}"

        # Parse Date from download file as this contains the recording date
        # https://download.binaergewitter.de/2023-12-30.Binaergewitter.Talk.328.mp3
        record_date_str = (
            e.links[1]
            .href.replace("https://download.binaergewitter.de/", "")
            .split(".")[0]
        )

        ingo = int("ingo" in e.podcast_person)
        l33tname = int("l33tname" in e.podcast_person)
        madmas = int("madmas" in e.podcast_person)
        makefu = int("felix" in e.podcast_person)
        print(
            f'"{e.title}",{release_date_str},{record_date_str},Talk,{e.itunes_duration},{ingo},{l33tname},{madmas},{makefu},0,0'
        )
