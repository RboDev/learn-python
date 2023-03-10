import feedparser
import urllib

# Enter the URL of the podcast RSS feed
# Histoire
rss_url = "https://radiofrance-podcast.net/podcast09/rss_10076.xml"
# Bach du dimanche
rss_url = "https://radiofrance-podcast.net/podcast09/rss_18189.xml"

feed = feedparser.parse(rss_url)

# Iterate over each entry in the feed
for entry in feed.entries:
    # Extract the audio URL from the enclosure tag
    audio_url = entry.enclosures[0].href
    
    # Generate a filename based on the title of the podcast episode
    filename = f"{entry.title}.mp3"
    
    # Download the audio file and save it as an mp3 file
    urllib.request.urlretrieve(audio_url, filename)
    
    print(f"Downloaded {filename}")
