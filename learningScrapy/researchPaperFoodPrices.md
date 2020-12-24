consumer have a short memory
Companies are already taking advantage of it[link](https://en.wikipedia.org/wiki/Bread_price-fixing_in_Canada)

Neural network
paper
gather the data using neural network vs bs4

project 
based on my paper I want to expand

# project
create a html to cdom parser?
use a tree
start <word></endword>

<script type="text/javascript"> content </script>
what is important is the first worf after < to the first whitespace and then to </. <{html tag} {more shit}>content </{html tag}>
epoch 1 (?<=\<).+?(?=\>)
epoch 2 <.+?> (matches everything insides the html tags)

This is a bit more difficult using regex since we have JSON and html in one so the regex picks on th tags and its content
Maybe we can have scrapy build it for us

Paper:
scraping or how to gather data when there are no adequate dataset for the problem you are trying to solve.

available options for you
- selenium
- bs4
- scrapy
- html request
- Spalsh

As dataScientist we will focus on Scrapy because of its command line interface and JS support

simple and pure html website (xkcd)
modern websites shopping websites and how to parse JSON.
very complicated websites (wallmart)
    - Articles often stops where their knowledge ends. but I'd like to leave with a few questions and topics to learn more on

How to set your spider 

usefull skills:
- regex
- python classes (maybe a quick review for building a spider)
Since there are 

What limitations will you be faced?

how to create a spider that can create a tree from the html