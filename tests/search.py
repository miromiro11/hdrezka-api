import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import HdrezkaAPI.hdrezka as Hdrezka

rezka = Hdrezka.Hdrezka()
results = rezka.search("The Amazing Spiderman")
for result in results:
    print(result)
    print("\n\n")