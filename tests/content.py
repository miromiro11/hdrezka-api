import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import HdrezkaAPI.hdrezka as Hdrezka

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
