from setuptools import setup, find_packages


setup(
    name="arxivcheck",
    version="0.3.1",
    packages=find_packages(exclude=["build", ]),
    scripts=["arxivcheck/bin/arxivcheck"],
    install_requires=["future","unidecode", "feedparser", "bibtexparser", "doi2bib"],
    include_package_data=True,
    license="AGPLv3",
    description="Generate a bibtex given a arxiv id or title, check if published",
    author="Bruno Messias",
    author_email="messias.physics@gmail.com",
    download_url="https://github.com/bibcure/arxivcheck/archive/0.3.1.tar.gz",
    keywords=["bibtex", "arxiv", "science", "scientific-journals"],
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    url="https://github.com/bibcure/arxivcheck"
)
