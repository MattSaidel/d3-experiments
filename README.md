d3-experiments
==============

This repo will contain my data visualization experiments with D3.

Baby Names
----------

The file top10bubbles.html is a project that visualizes the top 10 names for African-American female babies born in 2009. I aquired the data from NYC Open  Data and selected this particular dataset due to its manageable size and intuitive structure. 

The chart in the HTML file however, only shows data for the top 10 names from that year. My initial project idea, to display bubbles the size of which was deterimed by the name count, did not scale to the full dataset. 

The .JSON file provided by New York City was not immediately amenable to visualization. I formatted the file and stripped the copious metadata using Python's JSON and CSV modules. 

I had to hack at the x and y scales to display the data. If possible I would like to make those elements more elegant.

This project is also posted on my personal [website](http://www.matthewsaidel.com).


TODO
----

1. Add mouseover functionality
2. Fixing scaling
3. Allow for the addition of remaining data
