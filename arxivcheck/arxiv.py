# from __future__ import unicode_literals
from __future__ import print_function
from builtins import str
import feedparser
from doitobib.crossref import get_bib_from_doi
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
bare_url = "http://export.arxiv.org/api/query"


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
          'nov', 'dec']


def get_arxiv_info(arxiv_id):
    found = False
    item = {}
    params = "?search_query=id:"+arxiv_id
    result = feedparser.parse(bare_url+params)
    if len(result.entries) > 0:
        found = True
        item = result.entries[0]
    return found, item


def generate_bib_from_arxiv(arxiv_item, arxiv_id):
    # arxiv_cat = arxiv_item.arxiv_primary_category["term"]
    journal = "arxiv:"+arxiv_id
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
         "ID": year+first_author[0]+arxiv_id,
         "title": title,
         "year": year,
         "author": authors,
         "ENTRYTYPE": "article"}]
    bib = BibTexWriter().write(bib)

    if str(type(bib)) != "<type 'unicode'>":
        bib = str.encode(bib)
        bib = str(bib, "utf-8")
    return bib


def check_arxiv_published(arxiv_id, abbrev_journal=False):
    found = False
    published = False
    bib = ""
    found, item = get_arxiv_info(arxiv_id)
    if found:
        if "arxiv_doi" in item:
            doi = item["arxiv_doi"]
            published, bib = get_bib_from_doi(doi, abbrev_journal)
        else:
            bib = generate_bib_from_arxiv(item, arxiv_id)
    return found, published, bib
