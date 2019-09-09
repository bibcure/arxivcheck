========
Examples
========

Given a arxiv id...
--------------------

.. code-block:: bash

   $ arxivcheck 1601.02785

Given a arxiv title
-------------------

.. code-block:: bash

    $ arxivcheck -t Periodic Table of Topological

Given a file of titles or ids
-----------------------------


.. code-block:: bash

    $ arxivcheck -i  arxivs.txt

check if has been published, and then returns the updated bib
return outputs like

.. code-block:: bash

    @article{2007Karianearxiv:math/0703567v2,
        author = {Kariane Calta and John Smillie},
        journal = {arxiv:math/0703567v2},
        title = {Algebraically periodic translation surfaces},
        url = {http://arxiv.org/abs/math/0703567v2},
        year = {2007}
    }

    @article{Bradlyn_2016,
        doi = {10.1126/science.aaf5037},
        url = {https://doi.org/10.1126%2Fscience.aaf5037},
        year = 2016,
        month = {jul},
        publisher = {American Association for the Advancement of Science ({AAAS})},
        volume = {353},
        number = {6299},
        pages = {aaf5037},
        author = {Barry Bradlyn and Jennifer Cano and Zhijun Wang and M. G. Vergniory and C. Felser and R. J. Cava and B. Andrei Bernevig},
        title = {Beyond Dirac and Weyl fermions: Unconventional quasiparticles in conventional crystals},
        journal = {Science}
    }