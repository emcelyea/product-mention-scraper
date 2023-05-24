# product-mention-scraper
Testing a ~~scraper~~ for keyword mentions on reddit

### Considerations
The ideal performance would be a user types in a keyword (i.e. spiderman) and a list of every occurence is returned.
This is untenable for a few reasons:

### Conclusion
* This was fairly successful, I didnt end up scraping but pushshift provides a pretty solid API for reddit (way better than Reddit).
* If you just search for an object i.e. 'carrots' you are going to get a ludicrous amount of noise around your search.
* I included a list of verbs that we also check for in the comments. So I want all comments around ('carrots', ['cook', 'plant'])

 ### TODO
 * figure out some way around the rate-limiting so I can pull more data from comments (100 per request but would be nice to get a ~a thousand comments to parse), I could achieve this by rewriting this on the FE and have users make requests instead of the server, or creating several API users (it is pretty easy to make multiple reddit accounts).
 * Move all the filtering and verb stuff to the frontend, this should just return the results, that was users can decide how to filter the data once they have it

