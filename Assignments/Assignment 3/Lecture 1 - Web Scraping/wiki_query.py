import urllib
from urllib.request import urlopen                                                                                                                                                            
from urllib.parse import quote 
from bs4 import BeautifulSoup
import unicodedata
from nltk.tokenize import word_tokenize
from urllib.error import HTTPError
import nltk
import sys



def get_wikipedia_content(term):
  try:
    site_string = "https://en.wikipedia.org/wiki/" + quote(term)
    site = urlopen(site_string)
    soup = BeautifulSoup(site, "html.parser")
    items = soup.select(".mw-parser-output > p")
    texts = [unicodedata.normalize("NFKD", elem.get_text()).strip() for elem in items if 
                              len(word_tokenize(elem.get_text())) > 2]
    for i, t in enumerate(texts):
      if t.startswith(term[0].upper()+term[1:]):
        texts = texts[i:]
        break
    print(' '.join(texts).strip())
  except HTTPError:
    print("There is no Wikipedia page for your term.")


if __name__ == "__main__":

    if len(sys.argv) == 2 and sys.argv[1] not in ['-h', '--help']:
        search_term = sys.argv[1]
        get_wikipedia_content(search_term)
    else:
        print("usage: python3 wiki_query.py TERM")
        exit()