from setuptools import setup, find_packages

readme = open('README.md','r')
README_TEXT = readme.read()
readme.close()

setup(
    name="arxivcheck",
    version="0.1.3",
    packages = find_packages(exclude=["build",]),
    scripts=["arxivcheck/bin/arxivcheck"],
    long_description = README_TEXT,
    install_requires=["future", "feedparser", "bibtexparser", "doitobib"],
    include_package_data=True,
    license="GPLv3",
    description="Generate a bibtex given a arxiv id, check if published",
    author="Bruno Messias",
    author_email="messias.physics@gmail.com",
    download_url="https://github.com/bibcure/arxivcheck/archive/0.1.3.tar.gz",
    keywords=["bibtex","arxiv", "science","scientific-journals"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    url="https://github.com/devmessias/arxivcheck"
)
