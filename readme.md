
# HdrezkAPI
![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

This project is an API wrapper designed to interact with a comprehensive movie database website, which hosts an extensive collection of films covering various genres, languages, and periods. The primary purpose of this wrapper is to provide a tool for exploring and understanding the capabilities of web APIs and data manipulation.




# Disclaimer

This API wrapper has been developed for educational purposes only. The creator of this wrapper does not endorse or promote piracy in any form. The primary goal of this project is to demonstrate the capabilities and uses of API interaction, data scraping, and manipulation techniques for educational and research purposes only.

## Acknowledgements

The creator acknowledges that the hdrezka website is known for hosting content without proper authorization from the copyright holders. The intent behind creating this wrapper is not to facilitate access to pirated content but to provide a programming example on how to interact with web APIs. Users of this wrapper are strongly discouraged from using it in any manner that violates copyright laws or supports piracy.

The creator urges all users to respect copyright laws and to use this tool responsibly. Any use of this wrapper to engage in or promote piracy is strictly against the creator's intentions and ethical standards.

## Legal Note

By using this API wrapper, you agree to use it in a manner that complies with all applicable laws and regulations. The creator will not be held liable for any misuse of this software or for any legal consequences that arise from such misuse. Users are responsible for ensuring their use of the wrapper is legal and in compliance with copyright laws.

## Installation

Install hdrezkapi with pip

```bash
pip install hdrezkapi
```
    
## Usage/Examples


Looking a movie up:
```python
import HdrezkAPI.hdrezka as Hdrezka

rezka = Hdrezka.Hdrezka()
results = rezka.search("The Amazing Spiderman")
for result in results:
    print(result)
```
Fetching movie infomration:
```python
import HdrezkAPI.hdrezka as Hdrezka

rezka = Hdrezka.Hdrezka()
results = rezka.search("The Amazing Spiderman")
if len(results) == 0:
    print("No results found")
    exit()
test = rezka.get_content_infromation(results[0]['url'])
print(test)
```
Fetching a stream:
```python
import HdrezkAPI.hdrezka as Hdrezka

rezka = Hdrezka.Hdrezka()
results = rezka.search("The Amazing Spiderman")
if len(results) == 0:
    print("No results found")
    exit()

test = rezka.get_content_infromation(results[0]['url'])
streams = rezka.get_content_video(
    test['post_id'], 
    test['translations']['English'], 
    content_type=test['content_type'],
)
print(streams['480p'][0])

}
```
