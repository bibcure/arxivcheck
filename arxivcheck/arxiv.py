from __future__ import unicode_literals
from __future__ import print_function
import feedparser
from doitobib.crossref import get_bib_from_doi
bare_url = "http://export.arxiv.org/api/query"


def get_arxiv_info(arxiv_id):
    found = False
    item = {}
    params = "?search_query=id:"+arxiv_id
    result = feedparser.parse(bare_url+params)
    if len(result.entries) > 0:
        found = True
        item = result.entries[0]
    return found, item


def check_arxiv_published(arxiv_id, abbrev_journal):
    found = False
    bib = ""
    found, item = get_arxiv_info(arxiv_id)
    if found:
        if "arxiv_doi" in item:
            doi = item["arxiv_doi"]
            found, bib = get_bib_from_doi(doi, abbrev_journal)
        # else:
            # bib = generate_bib_from(arxiv)
    return found, bib
