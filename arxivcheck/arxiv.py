# from __future__ import unicode_literals
from __future__ import print_function
from builtins import str
import feedparser
from doitobib.crossref import get_bib_from_doi
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote
bare_url = "http://export.arxiv.org/api/query"


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
          'nov', 'dec']


def ask_which_is(title, items):
    found = False
    result = {}
    question = "\t It is >>'{}' article?y(yes)|n(no)|q(quit)"
    for item in items:
        w = input(question.format(
            item["title"], title))
        if w == "y":
            found = True
            result = item
            break
        if w == "q":
            break
    return found, result


def get_arxiv_info(value, field="id"):
    found = False
    items = []
    params = "?search_query="+field+":"+quote(value)
    url = bare_url+params
    result = feedparser.parse(url)
    items = result.entries
    found = len(items) > 0
    return found, items


def generate_bib_from_arxiv(arxiv_item, value, field="id"):
    # arxiv_cat = arxiv_item.arxiv_primary_category["term"]
    if field == "ti":
        journal = "arxiv:"+arxiv_item["id"].split("http://arxiv.org/abs/")[1]
    else:
        journal = "arxiv:"+value
    url = arxiv_item.link
    title = arxiv_item.title
    authors = arxiv_item.authors
    first_author = authors[0]["name"].split(" ")
    authors = " and ".join([author["name"] for author in authors])
    published = arxiv_item.published.split("-")
    year = published[0]

    month = months[int(published[1])]
    bib = BibDatabase()
    bib.entries = [
        {"journal": journal,
         "month": month,
         "url": url,
         "ID": year+first_author[0]+journal,
         "title": title,
         "year": year,
         "author": authors,
         "ENTRYTYPE": "article"}]
    bib = BibTexWriter().write(bib)

    if str(type(bib)) != "<type 'unicode'>":
        bib = str.encode(bib)
        bib = str(bib, "utf-8")
    return bib


def check_arxiv_published(value, field="id", get_first=True):
    found = False
    published = False
    bib = ""
    found, items = get_arxiv_info(value, field)
    if found:
        if get_first is False and field == "ti" and len(items) > 1:
            found, item = ask_which_is(value, items)
        else:
            item = items[0]
    if found:
        if "arxiv_doi" in item:
            doi = item["arxiv_doi"]
            published, bib = get_bib_from_doi(doi)
        else:
            bib = generate_bib_from_arxiv(item, value, field)
    return found, published, bib
