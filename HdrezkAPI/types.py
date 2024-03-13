from typing import TypedDict, List


TypeMovie = "movie"
TypeSeries = "series"


# [{'english_name': 'The Witcher, сериал, 2019 - ...', 'rating': '7.19', 'link': 'https://hdrezka.website/series/action/32556-vedmak-2019.html'}, {'english_name': 'The Witcher: Nightmare of the Wolf, аниме, 2021', 'rating': '6.86', 'link': 'https://hdrezka.website/animation/adventures/40712-vedmak-koshmar-volka-2021.html'}, {'english_name': 'The Witcher: Blood Origin, сериал, 2022', 'rating': '4.28', 'link': 'https://hdrezka.website/series/fantasy/51889-vedmak-proishozhdenie-2022.html'}, {'english_name': 'Making the Witcher, 2020', 'rating': '', 'link': 'https://hdrezka.website/films/documentary/62044-vedmak-kak-sozdavalsya-serial-2020.html'}]

class QueryResult(TypedDict):
    english_name: str
    rating: float
    url: str

class ContentInfo(TypedDict):
    post_id: str
    name: str
    translations: dict[str, str]
    content_type: str
    season: int
    episodes: int

#type that is string: list[str] 
ContentData = dict[str, List[str]]