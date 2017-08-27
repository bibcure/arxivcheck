from __future__ import unicode_literals, print_function, absolute_import
from builtins import input
import feedparser
from doi2bib.crossref import get_bib_from_doi
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote
import re
from unidecode import unidecode
bare_url = "http://export.arxiv.org/api/query"

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct',
          'nov', 'dec']


def ask_which_is(title, items):
    found = False
    result = {}
    question = "\n\tArxiv:{} \n\tIt is \n\t{}\n\t Correct?y(yes)|n(no)|q(quit)"
    for item in items:
        w = input(question.format(
            unidecode(item["title"]), unidecode(title)))
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
    params = "?search_query="+field+":"+quote(unidecode(value))
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
    if len(authors) > 0:
        first_author = authors[0]["name"].split(" ")
        authors = " and ".join([author["name"] for author in authors])
    else:
        first_author = authors
        authors = authors

    published = arxiv_item.published.split("-")
    year = ''
    if len(published) > 1:
        year = published[0]
    bib = BibDatabase()
    bib.entries = [
        {
            "journal": journal,
            "url": url,
            "ID": year+first_author[0]+journal,
            "title": title,
            "year": year,
            "author": authors,
            "ENTRYTYPE": "article"
        }
    ]
    bib = BibTexWriter().write(bib)
    return bib


def get_arxiv_pdf_link(value, field="id"):
    link = None
    value = re.sub("arxiv\:", "", value, flags=re.I)
    found, items = get_arxiv_info(value, field)
    if found:
        arxiv_item = items[0]
        pdf_item = list(
            filter(
                lambda i: i["type"] == "application/pdf",
                arxiv_item.links
            )
        )
        found = len(pdf_item) > 0
        link = pdf_item[0]["href"] if found else None

    return found, link


def check_arxiv_published(value, field="id", get_first=True):
    found = False
    published = False
    bib = ""
    value = re.sub("arxiv\:", "", value, flags=re.I)
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
    else:
        print("\t\nArxiv not found.")
    return found, published, bib
