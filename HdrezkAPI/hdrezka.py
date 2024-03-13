from HdrezkaAPI.common import formatResponses, decoder, formatDecodedData
from HdrezkaAPI.types import QueryResult,ContentInfo, ContentData
import httpx
import time
import json 
import bs4

BASE_URL = "https://hdrezka.website/"

class Hdrezka:
    #since there are mutliple mirrors of the site, the url can be changed if the site is down/changed
    def __init__(self, url: str = BASE_URL):
        self.url = url
        self.client = httpx.Client()

    #searches for a movie/show (not guaranteed to be accurate)
    def search(self, query: str) -> list[QueryResult]:
        toReturn = []
        response = self.client.post('https://hdrezka.website/engine/ajax/search.php', 
            data={
                "q": query
            },
            headers={
                "sec-ch-ua":        '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
                "rtt":              "50",
                "sec-ch-ua-mobile": "?0",
                "user-agent":       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "accept":           "text/html,*/*",
                "x-requested-with": "XMLHttpRequest",
                "downlink":         "3.9",
                "ect":              "4g",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-site":   "same-origin",
                "sec-fetch-mode":   "cors",
                "sec-fetch-dest":   "empty",
                "accept-encoding":  "gzip, deflate, br",
                "accept-language":  "en,en_US;q=0.9",
        })
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        lis = soup.find_all('li')
        for li in lis:
            toReturn.append(formatResponses(li))
        return toReturn
    
    #gets the content information, doesnt get the links and the quality, use get_content_video for that
    def get_content_infromation(self, url: str, season=None) -> ContentInfo:
        toReturn = {}
        if season:
            url = f"{url}#t:56-s:{season}-e:1"
        response = self.client.get(url, headers={
            "sec-ch-ua":        "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "rtt":              "50",
            "sec-ch-ua-mobile": "?0",
            "user-agent":       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "accept":           "text/html,*/*",
            "x-requested-with": "XMLHttpRequest",
            "downlink":         "3.9",
            "ect":              "4g",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-site":   "same-origin",
            "sec-fetch-mode":   "cors",
            "sec-fetch-dest":   "empty",
            "accept-encoding":  "gzip, deflate, br",
            "accept-language":  "en,en_US;q=0.9",

        })
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        post_id = soup.find(id="post_id")["value"]
        translations = soup.find(id="translators-list").find_all("li")
        for translation in translations:
            title = translation['title']
            if title == "Оригинал (+субтитры)":
                title = "English"
            translation_id = translation['data-translator_id']
            toReturn[title] = translation_id
        name = soup.find(class_='b-post__origtitle').text
        toReturn = {
            "post_id": post_id,
            "name": name,
            "translations": toReturn,
        }
        content_type = "movie"
        if "sof.tv.initCDNSeriesEvents" in response.text:
            content_type = "series"
            toReturn['content_type'] = content_type
            seasons = soup.find(
                id="simple-seasons-tabs").find_all("li")[-1]['data-tab_id']
            episodes = soup.find(id="simple-episodes-tabs").find_all("li")[-1]
            toReturn['seasons'] = int(seasons)
            toReturn['episodes'] = int(episodes['data-episode_id'])
        toReturn['content_type'] = content_type
        return toReturn

    #gets the video link and the quality
    def get_content_video(
        self, 
        contentId: str, 
        translationId: str, 
        content_type: str, 
        season: int = 1, 
        episode: int = 1
    ) -> ContentData: 
        data = {
            "id": contentId,
            "translator_id": translationId,
            "action": "get_movie" if content_type == "movie" else "get_episodes",
        }
        if content_type == "series":
            data["season"] = season
            data["episode"] = episode
        #not sure if t mattees but it is in the original code so I will keep it
        response = self.client.post(f'https://hdrezka.website/ajax/get_cdn_series/?t={round(time.time())}', headers={
            "sec-ch-ua":        "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "rtt":              "50",
            "sec-ch-ua-mobile": "?0",
            "user-agent":       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "accept":           "text/html,*/*",
            "x-requested-with": "XMLHttpRequest",
            "downlink":         "3.9",
            "ect":              "4g",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-site":   "same-origin",
            "sec-fetch-mode":   "cors",
            "sec-fetch-dest":   "empty",
            "accept-encoding":  "gzip, deflate, br",
            "accept-language":  "en,en_US;q=0.9",
        }, data=data)
        jsoned = {}
        try:
            jsoned = json.loads(response.text)
        except:
            return None
        if not jsoned['success']:
            return None
        decodedStreams = decoder(jsoned["url"])
        decodedStreams = formatDecodedData(decodedStreams)
        decodedStreams['movieId'] = contentId
        return decodedStreams
