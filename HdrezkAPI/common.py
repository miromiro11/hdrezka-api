import base64

#removes trash and decodes the base64 string
def decoder(todecode):
    trash = [
        "//_//JCQhIUAkJEBeIUAjJCRA",
        "//_//QEBAQEAhIyMhXl5e",
        "//_//IyMjI14hISMjIUBA",
        "//_//Xl5eIUAjIyEhIyM=",
        "//_//JCQjISFAIyFAIyM=",
    ]
    for i in trash:
        todecode = todecode.replace(
            i, "")

    return base64.b64decode(todecode[2:]).decode("utf-8")

#reformatting the lis found in the search function to a more readable format
def formatResponses(response):
    a = response.find("a")
    englishName = a.text.split("(")[1].split(")")[0]
    rating = a.text.split(")")[1]
    link = a["href"]
    return {
        "english_name": englishName,
        "rating": rating,
        "url": link
    }

def formatDecodedData(data):
    toReturn = {}
    splitted = data.split(',')
    for i in splitted:
        splitted2 = i.split(']')
        quality = splitted2[0].replace('[', '')
        links = splitted2[1].split(' or ')
        links = [i for i in links if "m3u8" not in i]
        toReturn[quality] = links
    return toReturn