import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import HdrezkaAPI.hdrezka as Hdrezka

rezka = Hdrezka.Hdrezka()
results = rezka.search("The Amazing Spiderman")
if len(results) == 0:
    print("No results found")
    exit()
test = rezka.get_content_infromation(results[0]['url'])
print(test)