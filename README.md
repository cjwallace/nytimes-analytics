NYTimes Analytics
=================

This is a work in progress analysis on the lexical diversity of articles classified as belonging to different sections of
the New York Times.

- ```nytimes_pull.py``` is originaly Hilary Mason's (part of a ML class) and utilizes the NYT Article Search API to return the title
and a bunch of other stuff about an article. It now only returns a sample of the body text, so I wrote...
- ```souper.py```, when run on the command line, will request a URL of an article. It writes the tittle and body of that article to
a text file. This returns the full body text, assuming you have access to the article.
- ```profiler.py``` returns the length and lexical diversity (according to my own definition) of the text.

This stuff is yet to be chained together into an analysis, so it's just a bunch of tools.
